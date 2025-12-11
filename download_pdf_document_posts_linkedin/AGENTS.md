# Repository Guidelines

## Goal & Core Strategy
- Automate downloading PDF documents from a LinkedIn company feed using an asynchronous Python script.
- Environment: Python script-first (runs locally or inside Colab via `python linkedin_downloader.py ...`).
- Engine: Playwright Async API for dynamic DOM + infinite scroll.
- Concurrency: `aiohttp` for efficient, parallel file downloading.
- Workflow: Setup -> Extract -> Save metadata -> Download -> Archive.

## Project Structure & Module Organization
- `linkedin_downloader.py` is the single, canonical workflow. It installs/uses Playwright, extracts LinkedIn document URLs asynchronously, downloads PDFs with `aiohttp`, and bundles outputs.
- Generated artifacts: `document_urls.txt` and `document_info.json` (URL list and metadata), `downloads/` (fetched PDFs), and `linkedin_documents.zip` (archive of downloads). Keep these out of version control.
- Core async functions: `extract_document_urls_async` (scrolls the company feed, finds `media.licdn.com` document links) and `download_documents_async` (streams PDFs).

## Key Components
- `extract_document_urls_async(company_url, max_scrolls)`: launches Chromium, navigates to feed, scrolls politely (stop when height stops growing), scans `a`/`iframe`/`embed` sources for `media.licdn.com/dms/document`, dedupes on full document URL.
- `download_documents_async(urls, output_dir='downloads')`: uses `aiohttp.ClientSession`, streams downloads with polite delay, extracts filenames from `Content-Disposition` when present.
- Expected outputs: `document_urls.txt`, `document_info.json`, `downloads/` PDFs, and `linkedin_documents.zip` (ignore all in git).

## Implementation Steps (Python script)
- Workflow order: Setup environment → run `python linkedin_downloader.py` (defaults: headless mode, 40 scrolls, feed URL `https://www.linkedin.com/company/target-teal/posts/?feedView=documents`) → Save metadata → Download → Archive.
- Authentication: set `LI_AT_COOKIE` if available; if absent/invalid the script immediately opens a visible browser for manual login, captures `li_at`, then returns to headless scraping. Optional `LINKEDIN_USER_DATA_DIR` env lets you reuse a logged-in Chrome profile.
- Environment: Python script-first (works locally or inside Colab by invoking the script); Playwright Async API for scrolling/DOM; `aiohttp` for concurrent downloads.
- Extraction (`extract_document_urls_async`): launch Chromium, politely scroll (wait for height changes), hover up to 5 visible document players to trigger manifest/PDF requests, wait for loaders to disappear, poll Performance API each scroll for `media.licdn.com/dms/document` resources, regex-scan page HTML for `feedshare-document-master-manifest` URLs, harvest storage, scan `a`/`iframe`/`embed` for `media.licdn.com/dms/document` URLs, dedupe on full document URL.
- Downloads (`download_documents_async`): use `aiohttp.ClientSession`, stream to disk in `downloads/`, respect polite delays between requests, derive filenames from `Content-Disposition` when present.
- Expected outputs: `document_urls.txt`, `document_info.json`, `downloads/` PDFs, and `linkedin_documents.zip` (keep all ignored by git).

## Operational Guardrails
- Context & rate limits: when LinkedIn shows HTTP 429 or ERR_TOO_MANY_REDIRECTS, back off for a few minutes, lower the scroll count (e.g., 10–15 by temporarily adjusting `DEFAULT_MAX_SCROLLS`), and increase scroll delay to ease load.
- Session reuse: prefer setting `LINKEDIN_USER_DATA_DIR` to a logged-in Chrome profile to avoid repeated cookie prompts; if a run fails mid-way, you can restart using the same profile and cached `document_urls.txt`.
- Rate limiting: `asyncio.sleep` between scrolls (~2s) and downloads (~1s) to avoid anti-bot triggers.
- Error handling: wrap navigation/extraction; log 4xx/5xx download errors without stopping the batch.
- Retries: polite exponential backoff (e.g., 3 tries) for transient download failures.
- Logging: minimal, English status lines (e.g., "✓ Saved…", "✗ Error…").

## Build, Test, and Development Commands
- Local: create a venv, install deps, install browser, then run the script:
  ```bash
  python -m venv .venv && source .venv/bin/activate
  pip install playwright aiohttp
  playwright install chromium
  LI_AT_COOKIE="<li_at>" python linkedin_downloader.py
  ```
- Colab (if used): install deps then call the script via `python linkedin_downloader.py` instead of running notebook cells.
- Re-run extraction/downloads by re-invoking `python linkedin_downloader.py`; adjust `LI_AT_COOKIE` or `LINKEDIN_USER_DATA_DIR` as needed.

## Coding Style & Naming Conventions
- Use 4-space indentation, keep everything async-first, and name coroutines with the `_async` suffix. Provide clear docstrings for functions.
- Keep modules linear and focused; avoid mixing shell commands with Python logic (even in Colab).
- Keep print output minimal and informative; favor English status lines for broader readability.

## Testing & Verification
- Manual only: run `LI_AT_COOKIE="<li_at>" python linkedin_downloader.py` and confirm counts and saved files match expectations.
- For download changes, verify a small sample (2–3 URLs) saves to `downloads/` with non-empty files and that `linkedin_documents.zip` is produced.
- When adding new parsing logic, add temporary debug logging to print detected URLs and remove or comment it before sharing.

## Commit & Pull Request Guidelines
- No existing git history is available; default to Conventional Commits (`feat:`, `fix:`, `docs:`, `chore:`) with concise scopes (e.g., `feat: improve iframe scraping`).
- In pull requests, include: purpose of the change, affected cells/sections, before/after behavior (counts, timings, or sample URLs), and any manual verification steps performed. Screenshots of notebook output are useful when UI results change.

## Security & Data Handling
- Do not hard-code credentials, cookies, or personal LinkedIn URLs. Keep any session data or downloaded documents out of the repository.
- If runtime authentication is needed, inject `li_at` at runtime only—never commit it or any session-bearing outputs.
- Respect target-site terms of service; avoid aggressive scroll counts or request rates, and consider adding polite delays if scaling up downloads.
