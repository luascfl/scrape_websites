#!/usr/bin/env python3
"""Trabalho com títulos de PDFs (renomear e ajustar metadados).

Modos principais:
- Dry run de renomeação: calcula títulos automaticamente e grava tabela/cache
  `python rename_pdfs.py`
- Aplicar renomeação recalculando: `python rename_pdfs.py --apply`
- Aplicar renomeação usando cache do dry run: `python rename_pdfs.py --apply-from-cache`

- Modo interativo para definir o título correto e gravar em metadados (opcional
  renomear):
  `python rename_pdfs.py --interactive [--rename-selected]`
  Em cada PDF, mostra comparativo de candidatos (metadados, 1ª página, 2ª
  página, fallback) e pergunta qual usar; grava o Title do PDF com a escolha.

No dry run, o script grava uma tabela em Markdown e um cache JSON para
reaproveitar os títulos sem recalcular. O modo interativo pergunta antes de
gravar e pode usar OCR para casos de imagem.

Requires poppler tools (`pdfinfo`, `pdftotext`); OCR step uses `pdftoppm` +
`tesseract` if available. Run from the folder that contains the PDFs or pass
`--dir /path/to/pdfs`.
"""

import argparse
import json
import os
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
import unicodedata
import textwrap
from collections import defaultdict
from typing import Iterable, Optional


STOP_PHRASES = [
    "design organizacional informado pela complexidade",
    "@target.teal",
    "target.teal",
    "continue >",
]


def have(binary: str) -> bool:
    return shutil.which(binary) is not None


def run(cmd: Iterable[str]) -> Optional[str]:
    try:
        out = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return out.stdout
    except Exception:
        return None


def get_meta_title(path: str) -> Optional[str]:
    out = run(["pdfinfo", path])
    if not out:
        return None
    for line in out.splitlines():
        if line.startswith("Title:"):
            val = line.split(":", 1)[1].strip()
            if val:
                return val
    return None


def normalize_line(line: str) -> str:
    line = re.sub(r"^[-•·\u2022\d\s\.\/]+", "", line)
    line = " ".join(line.split())
    return line.strip()


def should_ignore_line(line_lower: str) -> bool:
    if not line_lower:
        return True
    if re.fullmatch(r"[0-9]+/?[0-9]*", line_lower):
        return True
    for phrase in STOP_PHRASES:
        if phrase in line_lower:
            return True
    if line_lower.startswith("por "):
        return True
    return False


def extract_title_from_text(text: str) -> Optional[str]:
    blocks = []
    current = []
    for raw in text.splitlines():
        line = normalize_line(raw)
        lower = line.lower()
        if should_ignore_line(lower):
            if current:
                blocks.append(" ".join(current))
                current = []
            continue
        if line:
            current.append(line)
        elif current:
            blocks.append(" ".join(current))
            current = []
    if current:
        blocks.append(" ".join(current))
    for blk in blocks:
        blk_clean = re.sub(r"^c[oó]pia de\s+", "", blk, flags=re.IGNORECASE).strip()
        if re.search(r"[A-Za-zÀ-ÿ]", blk_clean) and len(blk_clean) >= 4:
            return blk_clean
    return None


def get_pdftotext_title(path: str, page: int = 1) -> Optional[str]:
    out = run(["pdftotext", "-f", str(page), "-l", str(page), "-nopgbrk", path, "-"])
    return extract_title_from_text(out or "") if out else None


def get_ocr_title(path: str) -> Optional[str]:
    if not (have("pdftoppm") and have("tesseract")):
        return None
    try:
        with tempfile.TemporaryDirectory() as td:
            prefix = os.path.join(td, "page")
            ppm = subprocess.run(
                ["pdftoppm", "-f", "1", "-l", "1", "-singlefile", "-png", path, prefix],
                capture_output=True,
            )
            if ppm.returncode != 0:
                return None
            img_path = prefix + ".png"
            ocr = subprocess.run(
                ["tesseract", img_path, "stdout", "-l", "por+eng", "--psm", "6"],
                capture_output=True, text=True,
            )
            if ocr.returncode != 0:
                return None
            return extract_title_from_text(ocr.stdout)
    except Exception:
        return None


def looks_meaningful(title: Optional[str], stem: str) -> bool:
    if not title:
        return False
    t = title.strip()
    if not t or len(t) < 4:
        return False
    tl = t.lower()
    if tl.startswith("copia de "):
        return False
    if tl in {"sem titulo", "sem título", "sem titulo-1", "sem título-1", "sem título-2", "sem titulo-2"}:
        return False
    if tl.replace(" ", "") == stem.lower().replace(" ", ""):
        return False
    if re.fullmatch(r"\d+", t):
        return False
    return True


def slugify(title: str) -> str:
    normalized = unicodedata.normalize("NFKD", title).encode("ascii", "ignore").decode("ascii")
    slug = re.sub(r"[^A-Za-z0-9]+", "-", normalized)
    return slug.strip("-").lower() or "untitled"


def choose_title(path: str, stem: str) -> str:
    meta = get_meta_title(path)
    meta_clean = re.sub(r"^c[oó]pia de\s+", "", meta, flags=re.IGNORECASE) if meta else None
    if looks_meaningful(meta_clean, stem):
        return meta_clean.strip()

    txt_title = get_pdftotext_title(path)
    if looks_meaningful(txt_title, stem):
        return txt_title.strip()

    ocr_title = get_ocr_title(path)
    if looks_meaningful(ocr_title, stem):
        return ocr_title.strip()

    return stem


def collect_candidates(path: str, stem: str, use_ocr: bool = False):
    candidates = []  # list of (source, title)
    seen = set()

    def add(source: str, title: Optional[str]):
        if not title:
            return
        t = title.strip()
        if not t:
            return
        if source != "arquivo" and not looks_meaningful(t, stem):
            return
        key = t.lower()
        if key in seen:
            return
        seen.add(key)
        candidates.append((source, t))

    meta = get_meta_title(path)
    meta_clean = re.sub(r"^c[oó]pia de\s+", "", meta, flags=re.IGNORECASE) if meta else meta
    add("metadata", meta_clean)

    p1 = get_pdftotext_title(path, page=1)
    add("pagina1", p1)

    p2 = get_pdftotext_title(path, page=2)
    add("pagina2", p2)

    if use_ocr:
        ocr = get_ocr_title(path)
        add("ocr", ocr)

    add("arquivo", stem)
    return candidates


def pick_default_index(candidates):
    if not candidates:
        return None
    priority = {"metadata": 0, "pagina2": 1, "pagina1": 2, "arquivo": 3}
    best_idx = 0
    best_score = 99
    for idx, (src, _) in enumerate(candidates):
        score = priority.get(src, 50)
        if score < best_score:
            best_score = score
            best_idx = idx
    return best_idx


def prompt_choice(pdf_name: str, candidates):
    print(f"\n=== {pdf_name} ===")
    if not candidates:
        print("Sem candidatos; pulando.")
        return None, None

    default_idx = pick_default_index(candidates)
    for i, (src, title) in enumerate(candidates, 1):
        display = textwrap.shorten(title, width=120, placeholder="…")
        print(f"[{i}] ({src}) {display}")
    print("[0] pular / manter como está")
    print("[m] digitar manualmente")
    prompt = "Escolha o número (Enter para padrão)" if default_idx is not None else "Escolha o número"
    choice = input(f"{prompt}: ").strip().lower()

    if choice == "0":
        return None, None
    if choice == "m":
        manual = input("Digite o título que deseja usar: ").strip()
        return manual or None, "manual"
    if choice == "" and default_idx is not None:
        src, title = candidates[default_idx]
        return title, src
    try:
        num = int(choice)
        if 1 <= num <= len(candidates):
            src, title = candidates[num - 1]
            return title, src
    except ValueError:
        pass
    print("Entrada inválida; usando padrão.")
    if default_idx is None:
        return None, None
    src, title = candidates[default_idx]
    return title, src


def set_pdf_title(path: pathlib.Path, title: str) -> bool:
    cmd = ["exiftool", "-overwrite_original", f"-Title={title}", str(path)]
    try:
        subprocess.run(cmd, capture_output=True, text=True, check=True)
        return True
    except subprocess.CalledProcessError as exc:
        print(f"[ERRO] {path.name}: {exc.stderr.strip()}")
        return False


def run_interactive(base_dir: pathlib.Path, rename_selected: bool, use_ocr: bool, markdown_path: pathlib.Path) -> None:
    if not have("exiftool"):
        sys.exit("exiftool é necessário para gravar metadados")

    pdfs = sorted(p for p in base_dir.iterdir() if p.suffix.lower() == ".pdf")
    if not pdfs:
        sys.exit("No PDFs found")

    used = defaultdict(int)
    summary = []  # (orig, chosen, source, final_name)

    for pdf in pdfs:
        candidates = collect_candidates(str(pdf), pdf.stem, use_ocr=use_ocr)
        chosen_title, source = prompt_choice(pdf.name, candidates)
        if not chosen_title:
            summary.append((pdf.name, "(pulado)", source or "", pdf.name))
            continue

        ok = set_pdf_title(pdf, chosen_title)
        final_name = pdf.name

        if ok and rename_selected:
            base = slugify(chosen_title)
            used[base] += 1
            suffix = "" if used[base] == 1 else f"-{used[base]}"
            new_name = f"{base}{suffix}.pdf"
            dst = base_dir / new_name
            if dst.exists():
                print(f"[SKIP rename] destino já existe: {dst.name}")
            elif new_name == pdf.name:
                pass
            else:
                pdf.rename(dst)
                print(f"[RENOMEADO] {pdf.name} -> {new_name}")
                final_name = new_name
        summary.append((pdf.name, chosen_title, source or "", final_name))

    # write summary markdown
    def esc(text: str) -> str:
        return text.replace("|", "\\|")

    lines = [
        "# Interativo – títulos escolhidos",
        "",
        "| Original | Título escolhido | Fonte | Nome final |",
        "| --- | --- | --- | --- |",
    ]
    for orig, chosen, src, final_name in summary:
        lines.append(f"| {esc(orig)} | {esc(chosen)} | {esc(src)} | {esc(final_name)} |")
    markdown_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"\nResumo salvo em: {markdown_path}")


def proposals_to_markdown(proposals, path: pathlib.Path) -> None:
    def esc(text: str) -> str:
        return text.replace("|", "\\|")

    lines = [
        "# Dry run – renomeação de PDFs",
        "",
        "| Original | Título encontrado | Novo nome |",
        "| --- | --- | --- |",
    ]
    for old, title, new in proposals:
        lines.append(f"| {esc(old)} | {esc(title)} | {esc(new)} |")
    path.write_text("\n".join(lines), encoding="utf-8")


def write_cache(proposals, path: pathlib.Path) -> None:
    payload = [
        {"original": old, "title": title, "new_name": new}
        for old, title, new in proposals
    ]
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def load_cache(path: pathlib.Path):
    data = json.loads(path.read_text(encoding="utf-8"))
    proposals = [(item["original"], item["title"], item["new_name"]) for item in data]
    return proposals


def main() -> None:
    parser = argparse.ArgumentParser(description="Rename PDFs using real titles")
    parser.add_argument("--dir", default=".", help="Directory containing PDFs (default: current)")
    parser.add_argument("--apply", action="store_true", help="Actually rename files (auto cálculo)")
    parser.add_argument("--apply-from-cache", action="store_true", help="Rename using cached dry-run results (skips recalculation)")
    parser.add_argument("--interactive", action="store_true", help="Modo interativo para escolher título e gravar no metadata")
    parser.add_argument("--rename-selected", action="store_true", help="No modo interativo, renomear o arquivo usando o título escolhido")
    parser.add_argument("--with-ocr", action="store_true", help="Incluir OCR como fonte adicional de título (página 1)")
    parser.add_argument("--markdown", default="dry_run_results.md", help="Path to write markdown table (default: dry_run_results.md)")
    parser.add_argument("--cache", default="dry_run_cache.json", help="Path to dry-run cache (default: dry_run_cache.json)")
    args = parser.parse_args()

    if not have("pdfinfo") or not have("pdftotext"):
        sys.exit("pdfinfo/pdftotext are required (install poppler-utils)")

    base_dir = pathlib.Path(args.dir)
    if not base_dir.is_dir():
        sys.exit(f"Not a directory: {base_dir}")

    if args.interactive:
        run_interactive(
            base_dir,
            rename_selected=args.rename_selected,
            use_ocr=args.with_ocr,
            markdown_path=base_dir / args.markdown,
        )
        return

    proposals = []
    if args.apply_from_cache:
        cache_path = base_dir / args.cache
        if not cache_path.exists():
            sys.exit(f"Cache não encontrado: {cache_path}")
        proposals = load_cache(cache_path)
        args.apply = True  # aplicar sempre que usar cache
    else:
        pdfs = sorted(p for p in base_dir.iterdir() if p.suffix.lower() == ".pdf")
        if not pdfs:
            sys.exit("No PDFs found")

        used = defaultdict(int)
        for pdf in pdfs:
            stem = pdf.stem
            title = choose_title(str(pdf), stem)
            base = slugify(title)
            used[base] += 1
            suffix = "" if used[base] == 1 else f"-{used[base]}"
            new_name = f"{base}{suffix}.pdf"
            proposals.append((pdf.name, title, new_name))

    width_old = max(len(p[0]) for p in proposals)
    width_title = max(len(p[1]) for p in proposals)
    print(f"{'Original':<{width_old}} | {'Título encontrado':<{width_title}} | Novo nome")
    print("-" * (width_old + width_title + 15))

    collisions = []
    for old, title, new in proposals:
        print(f"{old:<{width_old}} | {title:<{width_title}} | {new}")
        collisions.append(new)

    if len(collisions) != len(set(collisions)):
        print("\n[!] Nome colide mesmo após sufixo. Ajuste manual antes de aplicar.")
        return

    # sempre gera artefatos de dry run (mesmo se for aplicar em seguida)
    md_path = base_dir / args.markdown
    cache_path = base_dir / args.cache
    proposals_to_markdown(proposals, md_path)
    write_cache(proposals, cache_path)
    print(f"\nTabela salva em: {md_path}")
    print(f"Cache salvo em: {cache_path}")

    if not args.apply:
        print("\nDry run (nada renomeado). Use --apply ou --apply-from-cache para executar.")
        return

    for old, _, new in proposals:
        if old == new:
            continue
        src = base_dir / old
        dst = base_dir / new
        if not src.exists():
            print(f"[SKIP] origem não existe (já foi movido?): {src}")
            continue
        if dst.exists():
            print(f"[SKIP] destino já existe: {dst}")
            continue
        src.rename(dst)
        print(f"[OK] {old} -> {new}")


if __name__ == "__main__":
    main()
