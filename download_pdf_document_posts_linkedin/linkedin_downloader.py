import asyncio
import json
import os
import pathlib
import re
from datetime import datetime, timezone
from typing import Iterable, List, Sequence

import aiohttp
from playwright.async_api import async_playwright


DEFAULT_FEED_URL = "https://www.linkedin.com/company/target-teal/posts/?feedView=documents"
DEFAULT_MAX_SCROLLS = 80
DEFAULT_HEADLESS = True
DOWNLOAD_DIR = pathlib.Path("downloads")
MANIFEST_DIR = pathlib.Path("manifests")
URLS_FILE = pathlib.Path("document_urls.txt")
INFO_FILE = pathlib.Path("document_info.json")
ZIP_FILE = pathlib.Path("linkedin_documents.zip")
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
)

class AuthError(Exception):
    """Raised when authentication is lost (redirect to login/checkpoint)."""


class AbortAuth(Exception):
    """Raised when user declines to provide authentication."""


class RedirectLoopError(Exception):
    """Raised when LinkedIn returns an ERR_TOO_MANY_REDIRECTS error page."""


def load_env_from_file(path: pathlib.Path = pathlib.Path(".env")) -> None:
    """Minimal .env loader (KEY=VALUE lines)."""
    if not path.is_file():
        return
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line or line.strip().startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip())


async def extract_document_urls_async(page, max_scrolls: int = 12, scroll_delay: float = 3.0) -> List[str]:
    """
    Scrolls the company feed and extracts LinkedIn document URLs from anchors/iframes.
    Polite scrolling stops when no new height is added.
    """
    urls = set()
    no_change_runs = 0
    stale_url_runs = 0

    # Capture network responses to media.licdn.com/dms/document (manifest/images/transcript URLs inside embeds)
    def handle_response(response) -> None:
        try:
            url = response.url
            if "media.licdn.com/dms/document" in url:
                urls.add(url.split("#")[0])
        except Exception:
            return

    page.on("response", handle_response)

    async def wait_for_loader_disappear(timeout_ms: int = 10000) -> None:
        """Wait for common LinkedIn loader elements to disappear to ensure content is ready."""
        selectors = [
            ".artdeco-loader__bars",
            "[class*='artdeco-spinner']",
            "li-icon[type='loader']",
        ]
        for sel in selectors:
            try:
                await page.wait_for_selector(sel, state="hidden", timeout=timeout_ms)
            except Exception:
                continue

    async def warm_up_document_players(max_players: int = 5) -> None:
        """Hover visible document players to trigger manifest/pdf requests."""
        try:
            wrappers = page.locator(".ssplayer-wrapper")
            count = min(await wrappers.count(), max_players)
            for idx in range(count):
                try:
                    el = wrappers.nth(idx)
                    await el.scroll_into_view_if_needed()
                    await el.hover(timeout=3000)
                    await page.wait_for_timeout(500)
                except Exception:
                    continue
        except Exception:
            return

    async def collect_resource_urls() -> None:
        """Collect resource URLs (e.g., master manifests) from the Performance API."""
        try:
            resources = await page.evaluate(
                """
                () => {
                    const entries = performance.getEntriesByType('resource');
                    return Array.from(new Set(entries.map(e => e.name).filter(u => u.includes('media.licdn.com/dms/document'))));
                }
                """
            )
            urls.update(resources)
        except Exception:
            return

    async def harvest_storage() -> None:
        """Harvest any document URLs stored in localStorage/sessionStorage."""
        try:
            stored = await page.evaluate(
                """
                () => {
                    const values = [];
                    const pushValues = (storage) => {
                        for (let i = 0; i < storage.length; i++) {
                            try {
                                const key = storage.key(i);
                                const val = storage.getItem(key);
                                values.push(key || '');
                                values.push(val || '');
                            } catch (e) { continue; }
                        }
                    };
                    pushValues(localStorage);
                    pushValues(sessionStorage);
                    return values.filter(v => typeof v === 'string' && v.includes('media.licdn.com/dms/document'));
                }
                """
            )
            urls.update([v.split('#')[0] for v in stored])
        except Exception:
            return

    manifest_pattern = re.compile(
        r"https?://media\.licdn\.com/dms/document/[^\s\"'<>]+/feedshare-document-master-manifest/[^\s\"'<>]+",
        re.IGNORECASE,
    )

    def clean_manifest_url(raw: str) -> str:
        cleaned = raw.replace("&amp;", "&").replace("\\/", "/").strip("\"' ")
        return cleaned.split("#")[0]

    async def harvest_html_manifests() -> None:
        """Parse the current DOM HTML for master manifest URLs via regex to handle lazy content."""
        try:
            html = await page.content()
            for match in manifest_pattern.findall(html):
                urls.add(clean_manifest_url(match))
        except Exception:
            return

    async def harvest_dom() -> None:
        found = await page.evaluate(
            """
            () => {
                const links = new Set();
                const elements = Array.from(document.querySelectorAll('a,iframe,embed,source'));
                for (const el of elements) {
                    const href = el.href || el.src || '';
                    if (href.includes('media.licdn.com/dms/document')) {
                        links.add(href.split('#')[0]);
                    }
                }
                return Array.from(links);
            }
            """
        )
        urls.update(found)

    async def wait_for_feed_ready(stable_checks: int = 3, delay_ms: int = 800) -> None:
        """
        Wait until the page signals full load and the scroll height stabilizes to avoid missing content.
        """
        try:
            await page.wait_for_load_state("networkidle")
        except Exception:
            await page.wait_for_load_state("domcontentloaded")

        stable_runs = 0
        last_height = await page.evaluate("document.body.scrollHeight")
        while stable_runs < stable_checks:
            await page.wait_for_timeout(delay_ms)
            current_height = await page.evaluate("document.body.scrollHeight")
            if current_height == last_height:
                stable_runs += 1
            else:
                stable_runs = 0
                last_height = current_height
        print(f"Page ready: height={last_height}")

    async def click_load_more_if_present() -> bool:
        try:
            selectors = [
                "button:has-text('Exibir mais')",
                "button:has-text('Exibir mais resultados')",
                "button[aria-label*='Exibir mais']",
                "button[aria-label*='Carregar mais']",
            ]
            for sel in selectors:
                button = page.locator(sel)
                if await button.count() > 0:
                    await button.first.click()
                    await page.wait_for_timeout(int(scroll_delay * 1000))
                    return True
        except Exception:
            return False
        return False

    await wait_for_feed_ready()

    current_index = 0

    for i in range(max_scrolls):
        before_urls = len(urls)

        wrappers = page.locator(
            ".ssplayer-wrapper, [data-ss-player-in-viewport='true'], .ssplayer-presentation-player"
        )
        count = await wrappers.count()
        if count == 0:
            await page.evaluate("() => window.scrollBy(0, Math.max(window.innerHeight * 0.4, 450))")
            await page.wait_for_timeout(int(scroll_delay * 1000))
            await click_load_more_if_present()
        elif current_index < count:
            try:
                el = wrappers.nth(current_index)
                await el.scroll_into_view_if_needed()
                await el.hover(timeout=3000)
                await page.wait_for_timeout(800)
            except Exception:
                pass

        await harvest_dom()
        await collect_resource_urls()
        await harvest_html_manifests()
        await wait_for_loader_disappear()
        await page.wait_for_timeout(int(scroll_delay * 1000))

        current_offset = await page.evaluate("window.scrollY")
        print(
            f"Scroll {i + 1}/{max_scrolls}: found={len(urls)} total_wrappers={count} current_index={current_index} offset={current_offset}"
        )
        current_url = page.url
        if "login" in current_url or "checkpoint" in current_url:
            raise AuthError("Redirected to login/checkpoint during extraction.")
        new_urls = len(urls) - before_urls
        if new_urls == 0:
            stale_url_runs += 1
        else:
            stale_url_runs = 0

        if count == 0:
            no_change_runs += 1
        elif current_index < count - 1:
            current_index += 1
            no_change_runs = 0
        else:
            current_index = count
            no_change_runs += 1
            clicked = await click_load_more_if_present()
            if clicked:
                no_change_runs = 0

        if no_change_runs >= 4 or stale_url_runs >= 4:
            break

    try:
        perf_urls = await page.evaluate(
            """
            () => {
                const entries = performance.getEntriesByType('resource');
                return Array.from(new Set(entries.map(e => e.name).filter(u => u.includes('media.licdn.com/dms/document'))));
            }
            """
        )
        urls.update(perf_urls)
    except Exception:
        pass

    await harvest_storage()

    def prioritize(document_urls: List[str]) -> List[str]:
        pdf_urls = [u for u in document_urls if "feedshare-document-pdf" in u]
        others = [u for u in document_urls if u not in pdf_urls]
        # Keep order deterministic for reproducibility
        return sorted(set(pdf_urls)) + sorted(set(others))

    return prioritize(list(urls))


async def fetch_with_retries(session: aiohttp.ClientSession, url: str, dest: pathlib.Path, retries: int = 3) -> bool:
    """Deprecated; use fetch_bytes_with_filename instead."""
    return False


async def fetch_bytes_with_filename(
    session: aiohttp.ClientSession, url: str, retries: int = 3
) -> tuple[bytes | None, str | None]:
    delay = 1.0
    for attempt in range(1, retries + 1):
        try:
            async with session.get(url, timeout=120) as resp:
                if resp.status != 200:
                    raise aiohttp.ClientError(f"HTTP {resp.status}")
                ctype = resp.headers.get("Content-Type", "")
                if "application/json" in ctype.lower():
                    raise aiohttp.ClientError(f"unexpected content-type {ctype}")
                ctype = resp.headers.get("Content-Type", "")
                if "application/json" in ctype.lower():
                    raise aiohttp.ClientError(f"unexpected content-type {ctype}")
                data = await resp.read()
                if not data:
                    raise aiohttp.ClientError("empty body")
                filename = resp.headers.get("Content-Disposition")
                return data, filename
        except Exception as exc:  # noqa: PERF203
            if attempt == retries:
                print(f"✗ Failed {url} after {attempt} attempt(s): {exc}")
                return None, None
            await asyncio.sleep(delay)
            delay *= 2
    return None, None


def sanitize_filename(name: str) -> str:
    clean = "".join(ch for ch in name if ch.isalnum() or ch in (" ", "-", "_", ".", "(", ")"))
    clean = clean.strip()
    return clean


def guess_filename_from_url(url: str) -> str:
    """Attempt to derive a human-friendly filename from the manifest or pdf URL."""
    # Try to extract a meaningful slug before query params
    path_part = url.split("?")[0]
    tail = path_part.rstrip("/").split("/")[-1]
    if tail.lower().endswith(".pdf"):
        return tail
    # Sometimes the ID is just digits; return it so dedup_name can append .pdf
    return tail or ""


def extract_pdf_title(data: bytes) -> str | None:
    """
    Try to extract the Title metadata from a PDF.
    Uses PyPDF2 if available; otherwise a lightweight regex fallback.
    """
    try:
        import io
        from PyPDF2 import PdfReader  # type: ignore

        reader = PdfReader(io.BytesIO(data))
        title = getattr(reader, "metadata", None)
        if title and getattr(title, "title", None):
            return str(title.title)
    except Exception:
        pass

    try:
        import re

        match = re.search(rb"/Title\s*\(([^)]{1,200})\)", data)
        if match:
            raw = match.group(1)
            try:
                return raw.decode("utf-8", errors="ignore")
            except Exception:
                return raw.decode("latin-1", errors="ignore")
    except Exception:
        pass
    return None


def parse_content_disposition_filename(header: str | None) -> str | None:
    if not header:
        return None
    parts = header.split(";")
    for part in parts:
        if "filename" in part:
            _, _, value = part.partition("=")
            value = value.strip().strip('"').strip("'")
            return value
    return None


async def download_documents_async(urls: Sequence[str], cookie: str, output_dir: pathlib.Path = DOWNLOAD_DIR) -> List[pathlib.Path]:
    """
    Streams document downloads with polite backoff. Returns paths of saved files.
    """
    if not urls:
        print("No URLs to download.")
        return []

    output_dir.mkdir(parents=True, exist_ok=True)
    headers = {"User-Agent": USER_AGENT}
    if cookie:
        headers["Cookie"] = f"li_at={cookie}"

    saved: List[pathlib.Path] = []
    seen_names: set[str] = set()

    pdf_only = [u for u in urls if "feedshare-document-pdf" in u]
    if len(pdf_only) != len(urls):
        print(f"Skipping {len(urls) - len(pdf_only)} non-PDF URLs.")
    urls = pdf_only

    def dedup_name(name: str) -> str:
        base = pathlib.Path(name).name or "document.pdf"
        if not base.lower().endswith(".pdf"):
            base = f"{base}.pdf"
        candidate = base
        idx = 1
        while candidate in seen_names:
            stem = pathlib.Path(base).stem
            suffix = pathlib.Path(base).suffix
            candidate = f"{stem}_{idx}{suffix}"
            idx += 1
        seen_names.add(candidate)
        return candidate

    async with aiohttp.ClientSession(headers=headers) as session:
        for url in urls:
            data, disp = await fetch_bytes_with_filename(session, url)
            if data is None:
                continue
            header_name = parse_content_disposition_filename(disp)
            # Fallback order: Content-Disposition > PDF Title > URL tail (numeric slug)
            fallback_name = guess_filename_from_url(url)
            title_name = extract_pdf_title(data)
            name = sanitize_filename(header_name or title_name or fallback_name)
            name = dedup_name(name)
            dest = output_dir / name
            dest.write_bytes(data)
            print(f"✓ Saved {dest} ({len(data)} bytes)")
            saved.append(dest)
            await asyncio.sleep(1.0)  # polite delay between downloads
    return saved


def write_metadata(urls: Iterable[str]) -> None:
    URLS_FILE.write_text("\n".join(urls), encoding="utf-8")
    timestamp = datetime.now(timezone.utc).isoformat()
    info = [
        {"url": url, "source": "media.licdn.com/dms/document", "timestamp": timestamp}
        for url in urls
    ]
    INFO_FILE.write_text(json.dumps(info, indent=2), encoding="utf-8")


def select_pdf_urls(urls: Sequence[str]) -> List[str]:
    """Return only feedshare-document-pdf(-analyzed) URLs, deduped."""
    seen = set()
    pdfs: List[str] = []

    for url in urls:
        if "feedshare-document-pdf" not in url:
            continue
        key = url.split("?")[0]
        if key in seen:
            continue
        seen.add(key)
        pdfs.append(url)

    return pdfs


async def expand_pdf_urls(urls: Sequence[str], cookie: str) -> List[str]:
    """
    Try to derive feedshare-document-pdf(-analyzed) URLs from manifests when not directly present.
    Also stores fetched manifests under manifests/.
    """
    pdf_urls = set(select_pdf_urls(urls))
    manifest_urls = [
        u
        for u in urls
        if "feedshare-document" in u
        and "manifest" in u
        and "feedshare-document-pdf" not in u
        and "feedshare-document-images" not in u
    ]
    # Fallback: any feedshare-document (non-pdf) if no manifest-like URL is present
    if not manifest_urls:
        manifest_urls = [u for u in urls if "feedshare-document" in u and "feedshare-document-pdf" not in u]
    if not manifest_urls:
        return list(pdf_urls)

    MANIFEST_DIR.mkdir(parents=True, exist_ok=True)
    headers = {"User-Agent": USER_AGENT}
    if cookie:
        headers["Cookie"] = f"li_at={cookie}"

    async with aiohttp.ClientSession(headers=headers) as session:
        for murl in manifest_urls:
            try:
                async with session.get(murl, timeout=30) as resp:
                    if resp.status != 200:
                        print(f"✗ Manifest fetch {resp.status}: {murl}")
                        continue
                    text = await resp.text()
                    # persist manifest for inspection/reuse
                    base = murl.split("/")[-1].split("?")[0] or "manifest"
                    dest = MANIFEST_DIR / f"{base}.json"
                    dest.write_text(text, encoding="utf-8")

                    found: set[str] = set()
                    # Regex fallback for any feedshare-document-pdf(-analyzed) URL
                    regex_hits = re.findall(r"https?://[^\\s\"']*feedshare-document-pdf[^\\s\"']+", text)
                    found.update(u.split("#")[0] for u in regex_hits)

                    # JSON parse to grab transcribedDocumentUrl if present
                    try:
                        data = json.loads(text)
                        stack = [data]
                        while stack:
                            current = stack.pop()
                            if isinstance(current, dict):
                                for key, val in current.items():
                                    if isinstance(val, str) and "feedshare-document-pdf" in val:
                                        found.add(val.split("#")[0])
                                    if key == "transcribedDocumentUrl" and isinstance(val, str):
                                        found.add(val.split("#")[0])
                                    stack.append(val)
                            elif isinstance(current, list):
                                stack.extend(current)
                            elif isinstance(current, str) and "feedshare-document-pdf" in current:
                                found.add(current.split("#")[0])
                    except Exception:
                        pass

                    if found:
                        print(f"✓ Found {len(found)} PDF URL(s) in manifest {base}")
                        pdf_urls.update(found)
            except Exception:
                continue
    return list(pdf_urls)


async def run(
    cookie: str,
    feed_url: str = DEFAULT_FEED_URL,
    max_scrolls: int = DEFAULT_MAX_SCROLLS,
    user_data_dir: str | None = None,
) -> None:
    """
    Default workflow: headless scraping (40 scrolls) with an automatic interactive
    login fallback to capture a fresh li_at cookie when needed.
    """
    async with async_playwright() as p:
        chromium_args = [
            "--disable-blink-features=AutomationControlled",
            "--disable-features=IsolateOrigins,site-per-process",
            "--disable-site-isolation-trials",
        ]
        headless_mode = DEFAULT_HEADLESS
        browser = None
        context = None
        page = None
        persistent_allowed = bool(user_data_dir)
        is_persistent = False

        async def create_context(desired_headless: bool) -> None:
            """(Re)create a browser context with the requested headless setting."""
            nonlocal browser, context, page, headless_mode, persistent_allowed, is_persistent
            headless_mode = desired_headless

            try:
                if context:
                    await context.close()
            except Exception:
                pass
            try:
                if browser:
                    await browser.close()
            except Exception:
                pass

            if persistent_allowed and user_data_dir:
                try:
                    context = await p.chromium.launch_persistent_context(
                        user_data_dir=user_data_dir,
                        headless=headless_mode,
                        viewport={"width": 1366, "height": 768},
                        user_agent=USER_AGENT,
                        args=chromium_args,
                    )
                    await context.add_init_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined});")
                    page = context.pages[0] if context.pages else await context.new_page()
                    browser = context.browser
                    is_persistent = True
                    return
                except Exception as exc:
                    if "ProcessSingleton" in str(exc):
                        print("⚠️ Persistent profile in use. Falling back to a temporary session.")
                        persistent_allowed = False
                    else:
                        raise

            browser = await p.chromium.launch(headless=headless_mode, args=chromium_args)
            context = await browser.new_context(
                user_agent=USER_AGENT,
                viewport={"width": 1366, "height": 768},
            )
            await context.add_init_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined});")
            page = await context.new_page()
            is_persistent = False

        async def reset_context(force_headless: bool | None = None) -> None:
            desired = headless_mode if force_headless is None else force_headless
            await create_context(desired)

        await create_context(headless_mode)

        async def wipe_storage() -> None:
            """Clear storage in the current context/page."""
            if not is_persistent:
                try:
                    await context.clear_cookies()
                except Exception:
                    pass
            try:
                await page.goto("https://www.linkedin.com", wait_until="domcontentloaded", timeout=60000)
                await page.evaluate("() => { localStorage.clear(); sessionStorage.clear(); }")
            except Exception:
                pass

        use_existing_only = False
        if URLS_FILE.is_file():
            use_existing_only = input("Use existing document_urls.txt and skip new extraction? (y/N): ").strip().lower() == "y"

        async def ensure_auth() -> None:
            nonlocal cookie
            nonlocal headless_mode
            tried = set()

            async def is_redirect_loop() -> bool:
                """Detect LinkedIn's too-many-redirects error page."""
                try:
                    if page.url.startswith("chrome-error://"):
                        return True
                    content = await page.content()
                    lowered = content.lower()
                    return "err_too_many_redirects" in lowered or "redirecionamento em excesso" in lowered
                except Exception:
                    return False

            async def recover_from_429_if_needed(max_retries: int = 2) -> None:
                """If the page shows an HTTP 429 error page, back off and retry a reload."""
                for attempt in range(max_retries):
                    try:
                        content = (await page.content()).lower()
                    except Exception:
                        content = ""
                    if "http error 429" not in content and "err_http_response_code_failure" not in content:
                        return
                    wait_for = 60 * (attempt + 1)
                    print(f"HTTP 429 page detected. Waiting {wait_for}s before retry {attempt + 1}/{max_retries}...")
                    await asyncio.sleep(wait_for)
                    try:
                        await page.goto(feed_url, wait_until="domcontentloaded", timeout=120000)
                    except Exception as exc:
                        print(f"⚠️ Retry navigation after 429 failed: {exc}")
                        continue
                raise AuthError("Stuck on HTTP 429 page after retries.")

            async def capture_cookie_via_manual_login(reason: str) -> None:
                """Open a visible browser to capture a fresh li_at, then return to headless scraping."""
                nonlocal cookie
                nonlocal headless_mode
                print(reason)
                await reset_context(force_headless=False)
                await wipe_storage()
                await page.goto("https://www.linkedin.com/login", wait_until="domcontentloaded", timeout=120000)
                print("Complete login in the opened window. Waiting up to 3 minutes...")
                try:
                    await page.wait_for_function(
                        "() => !location.href.includes('login') && !location.href.includes('checkpoint')",
                        timeout=180000,
                    )
                except Exception as exc:
                    raise RuntimeError("Login not completed in time. Please try again with a fresh session.") from exc
                if await is_redirect_loop():
                    await reset_context(force_headless=headless_mode)
                    raise AuthError("Redirect loop after manual login.")

                cookies_all = await context.cookies()
                li_at_cookie = next((c for c in cookies_all if c.get("name") == "li_at"), None)
                if not li_at_cookie:
                    await reset_context(force_headless=headless_mode)
                    raise AuthError("Could not capture li_at after manual login.")

                cookie_value = li_at_cookie.get("value", cookie)
                cookie = cookie_value or ""
                os.environ["LI_AT_COOKIE"] = cookie
                print("Captured fresh li_at from manual login. Continuing with visible session (no headless reset).")

                headless_mode = False

                try:
                    await context.add_cookies(cookies_all)
                except Exception:
                    pass
                response = None
                try:
                    response = await page.goto(feed_url, wait_until="networkidle", timeout=120000)
                except Exception as exc:
                    print(f"⚠️ Navigation error after manual login: {exc}")
                    if "Timeout" in str(exc):
                        try:
                            response = await page.goto(feed_url, wait_until="domcontentloaded", timeout=120000)
                        except Exception:
                            pass
                if not response and "linkedin.com/company" in page.url:
                    # Already on a company/feed page despite navigation error; continue.
                    return
                if response and response.status >= 400:
                    print(f"⚠️ Feed navigation returned HTTP {response.status} after login; continuing anyway.")
                if await is_redirect_loop() or "login" in page.url or "checkpoint" in page.url:
                    raise AuthError("Redirected to login/checkpoint after manual login.")
                await recover_from_429_if_needed()

            if is_persistent and not cookie:
                try:
                    response = await page.goto(feed_url, wait_until="networkidle", timeout=120000)
                    if response and response.status == 429:
                        raise AuthError("HTTP 429 while using persistent profile.")
                    if await is_redirect_loop():
                        raise RedirectLoopError("Redirect loop while using persistent profile.")
                    if "login" not in page.url and "checkpoint" not in page.url:
                        return
                except RedirectLoopError:
                    print("Redirect loop detected with existing persistent profile. Resetting the session.")
                    await reset_context(force_headless=headless_mode)
                except AuthError:
                    print("HTTP 429 encountered with persistent profile. Opening browser for manual login...")
                    await capture_cookie_via_manual_login("Opening browser to refresh session after 429...")
                    return
                except Exception:
                    pass

            if not cookie and not is_persistent:
                await capture_cookie_via_manual_login("No li_at cookie provided. Opening login to capture one...")
                return

            async def attempt_with_cookie(li_at_value: str) -> str:
                if not li_at_value or li_at_value in tried:
                    return "skip"
                tried.add(li_at_value)
                if not is_persistent:
                    await wipe_storage()
                cookie_record = {
                    "name": "li_at",
                    "value": li_at_value,
                    "domain": ".linkedin.com",
                    "path": "/",
                    "httpOnly": True,
                    "secure": True,
                    "sameSite": "None",
                }
                await context.add_cookies(
                    [
                        cookie_record,
                        {**cookie_record, "domain": ".www.linkedin.com"},
                        {**cookie_record, "domain": "www.linkedin.com"},
                    ]
                )
                try:
                    response = await page.goto(feed_url, wait_until="networkidle", timeout=120000)
                    if response and response.status == 429:
                        print("Received HTTP 429 when navigating with provided cookie.")
                        return "429"
                    if await is_redirect_loop():
                        raise RedirectLoopError("Redirect loop while using provided li_at cookie.")
                    if "login" not in page.url and "checkpoint" not in page.url:
                        return "ok"
                except RedirectLoopError:
                    raise
                except Exception:
                    return "fail"
                return "fail"

            try:
                result = await attempt_with_cookie(cookie)
                if result == "ok":
                    return
                if result == "429":
                    await capture_cookie_via_manual_login(
                        "HTTP 429 with provided cookie. Opening a visible browser for manual login..."
                    )
                    return
            except RedirectLoopError:
                print("Redirect loop detected with provided cookie. Resetting session and retrying...")
                await reset_context(force_headless=headless_mode)
                await wipe_storage()

            prompt = "li_at cookie invalid/expired. Paste a fresh li_at (leave blank to log in manually): "
            fresh = input(prompt).strip()
            if fresh:
                os.environ["LI_AT_COOKIE"] = fresh
                cookie = fresh
                try:
                    result = await attempt_with_cookie(fresh)
                    if result == "ok":
                        return
                    if result == "429":
                        await capture_cookie_via_manual_login(
                            "HTTP 429 with provided cookie. Opening a visible browser for manual login..."
                        )
                        return
                except RedirectLoopError:
                    print("Redirect loop detected with provided cookie. Resetting session and retrying...")
                    await reset_context(force_headless=headless_mode)
                    await wipe_storage()

            await capture_cookie_via_manual_login("Opening a visible browser for manual login to capture a fresh li_at...")

        aggregated_urls: set[str] = set()

        if use_existing_only and URLS_FILE.is_file():
            existing = [line.strip() for line in URLS_FILE.read_text(encoding="utf-8").splitlines() if line.strip()]
            aggregated_urls.update(existing)
            print(f"Using {len(aggregated_urls)} URL(s) from document_urls.txt.")
        else:
            attempts = 0
            while attempts < 3:
                try:
                    await ensure_auth()
                    batch = await extract_document_urls_async(page, max_scrolls=max_scrolls)
                    aggregated_urls.update(batch)
                    if aggregated_urls:
                        break
                except AbortAuth:
                    if URLS_FILE.is_file():
                        use_existing_fallback = input("Use existing document_urls.txt to download? (y/N): ").strip().lower() == "y"
                        if use_existing_fallback:
                            existing = [line.strip() for line in URLS_FILE.read_text(encoding="utf-8").splitlines() if line.strip()]
                            aggregated_urls.update(existing)
                            break
                    if browser:
                        await browser.close()
                    return
                except AuthError:
                    fresh = input("Session lost. Paste a fresh li_at to retry (leave blank to abort): ").strip()
                    if not fresh:
                        if URLS_FILE.is_file():
                            use_existing_fallback = input("Use existing document_urls.txt to download? (y/N): ").strip().lower() == "y"
                            if use_existing_fallback:
                                existing = [line.strip() for line in URLS_FILE.read_text(encoding="utf-8").splitlines() if line.strip()]
                                aggregated_urls.update(existing)
                                break
                        if browser:
                            await browser.close()
                        return
                    os.environ["LI_AT_COOKIE"] = fresh
                    cookie = fresh
                    attempts += 1
                    print("Retrying after authentication refresh...")
                    continue

                fresh = input("No document URLs found. Paste a fresh li_at to retry (leave blank to stop): ").strip()
                if not fresh:
                    break
                os.environ["LI_AT_COOKIE"] = fresh
                cookie = fresh
                attempts += 1
                print("Retrying with new cookie...")

        pdf_urls = await expand_pdf_urls(list(aggregated_urls), cookie)
        filtered_urls = select_pdf_urls(pdf_urls)
        print(f"Extracted {len(filtered_urls)} document URL(s) after filtering for PDFs.")
        if not filtered_urls:
            if browser:
                await browser.close()
            return
        write_metadata(filtered_urls)

        downloaded = await download_documents_async(filtered_urls, cookie, DOWNLOAD_DIR)
        print(f"Downloaded {len(downloaded)} file(s).")
        if browser:
            await browser.close()


def main() -> None:
    load_env_from_file()
    cookie = os.getenv("LI_AT_COOKIE", "") or ""
    user_data_dir = os.getenv("LINKEDIN_USER_DATA_DIR")

    try:
        asyncio.run(
            run(
                cookie=cookie,
                feed_url=DEFAULT_FEED_URL,
                max_scrolls=DEFAULT_MAX_SCROLLS,
                user_data_dir=user_data_dir,
            )
        )
    except KeyboardInterrupt:
        raise SystemExit("Interrupted by user.")


if __name__ == "__main__":
    main()
