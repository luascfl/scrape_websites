#!/bin/bash

# --- CONFIGURAÇÃO ---
ALVOS=(
    "https://docs.apollo.io"
    "https://teya.us"
    "https://novi.cc"
    "https://targetteal.com"
    "https://hyperisland.com.br"
    "https://toolboxtoolbox.com"
)
# --------------------

echo "Iniciando backup com suporte a CDN e Subdomínios..."

if [ -z "${MODO_TEXTOS:-}" ]; then
    read -r -p "Arquivos de texto existentes: [c] comparar data e substituir se mais recente / [p] pular se já existe? (c/p) " MODO_TEXTOS
fi
MODO_TEXTOS=${MODO_TEXTOS:-c}

for alvo in "${ALVOS[@]}"; do
    
    # Extração do domínio e limpeza de nomes
    dominio_raiz=$(echo "$alvo" | awk -F/ '{print $1 "//" $3}')
    dominio_www="https://www.${dominio_raiz#https://}"
    dominio_www="${dominio_www#http://}"
    dominio_www="${dominio_www%/}"
    nome_pasta=$(echo "$alvo" | sed -e 's|https://||g' -e 's|http://||g' -e 's|/$||g' -e 's|/|_|g')
    
    echo "--------------------------------------------------------"
    echo "Processando: $nome_pasta"
    mkdir -p "$nome_pasta/Textos"
    mkdir -p "$nome_pasta/PDFs"
    mkdir -p "$nome_pasta/Videos"

    # --- PASSO 1: MAPEAMENTO E FILTRO ---
    echo " > Gerando lista de artigos alvo..."
    # Tenta sitemap (https)
    trafilatura --sitemap "$dominio_raiz" --list 2>/dev/null | grep "$alvo" > "$nome_pasta/links_filtrados.txt"
    qtd=$(wc -l < "$nome_pasta/links_filtrados.txt")
    # Fallback: sitemap na versão www
    if [ "$qtd" -eq 0 ]; then
        trafilatura --sitemap "$dominio_www" --list 2>/dev/null | grep "$dominio_www" > "$nome_pasta/links_filtrados.txt"
        qtd=$(wc -l < "$nome_pasta/links_filtrados.txt")
    fi
    # Fallback: sitemap http
    if [ "$qtd" -eq 0 ]; then
        dominio_http=${dominio_raiz/https:\/\//http://}
        dominio_http_www=${dominio_www/https:\/\//http://}
        trafilatura --sitemap "$dominio_http" --list 2>/dev/null | grep "$dominio_http" > "$nome_pasta/links_filtrados.txt"
        qtd=$(wc -l < "$nome_pasta/links_filtrados.txt")
        if [ "$qtd" -eq 0 ]; then
            trafilatura --sitemap "$dominio_http_www" --list 2>/dev/null | grep "$dominio_http_www" > "$nome_pasta/links_filtrados.txt"
            qtd=$(wc -l < "$nome_pasta/links_filtrados.txt")
        fi
    fi

    # Fallback para sites sem sitemap ou com lista vazia (ex: novi.cc)
    if [ "$qtd" -eq 0 ]; then
        echo " ! Sitemap vazio. Tentando exploração rasa..."
        trafilatura --explore "$dominio_raiz" --list --url-filter "$dominio_raiz" 2>/dev/null | grep "$alvo" > "$nome_pasta/links_filtrados.txt"
        qtd=$(wc -l < "$nome_pasta/links_filtrados.txt")
        if [ "$qtd" -eq 0 ]; then
            trafilatura --explore "$dominio_www" --list --url-filter "$dominio_www" 2>/dev/null | grep "$dominio_www" > "$nome_pasta/links_filtrados.txt"
            qtd=$(wc -l < "$nome_pasta/links_filtrados.txt")
        fi
    fi

    # Fallback adicional sem paths específicos: crawl raso no domínio
    if [ "$qtd" -eq 0 ]; then
        echo " ! Exploração rasa falhou ou teve redirects. Tentando crawl limitado no domínio..."
        trafilatura --crawl "$dominio_raiz" --list --url-filter "$dominio_raiz" 2>/dev/null \
            | grep "$alvo" > "$nome_pasta/links_filtrados.txt" || true
        qtd=$(wc -l < "$nome_pasta/links_filtrados.txt")
        if [ "$qtd" -eq 0 ]; then
            trafilatura --crawl "$dominio_www" --list --url-filter "$dominio_www" 2>/dev/null \
                | grep "$alvo" > "$nome_pasta/links_filtrados.txt" || true
            qtd=$(wc -l < "$nome_pasta/links_filtrados.txt")
        fi
        if [ "$qtd" -eq 0 ]; then
            trafilatura --crawl "$dominio_http" --list --url-filter "$dominio_http" 2>/dev/null \
                | grep "$dominio_http" > "$nome_pasta/links_filtrados.txt" || true
            qtd=$(wc -l < "$nome_pasta/links_filtrados.txt")
        fi
        if [ "$qtd" -eq 0 ]; then
            trafilatura --crawl "$dominio_http_www" --list --url-filter "$dominio_http_www" 2>/dev/null \
                | grep "$dominio_http_www" > "$nome_pasta/links_filtrados.txt" || true
            qtd=$(wc -l < "$nome_pasta/links_filtrados.txt")
        fi
    fi

    if [ "$qtd" -eq 0 ]; then
        echo " ! Nenhum link encontrado. Pulando..."
        continue
    fi

    # --- PASSO 2: TEXTOS ---
    echo " > [1/3] Baixando textos... (com nomes amigáveis)"
    MODO_TEXTOS="$MODO_TEXTOS" python3 - <<'PY' "$nome_pasta/Textos" "$nome_pasta/links_filtrados.txt"
import os
import pathlib
import re
import sys
import unicodedata
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Lock

from dateutil import parser as dateparser
from trafilatura import extract, fetch_url, metadata

dest_dir = pathlib.Path(sys.argv[1])
links_file = pathlib.Path(sys.argv[2])

dest_dir.mkdir(parents=True, exist_ok=True)

def slugify(text: str) -> str:
    # Remove acentos e caracteres problemáticos para nomes de arquivos
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    # Converte espaços e barras em underscore
    text = re.sub(r"[\s/]+", "_", text)
    # Remove caracteres que não sejam letras, números, underscore, ponto ou hífen
    text = re.sub(r"[^\w.-]+", "", text)
    return text.strip("._") or "sem_titulo"

def parse_date(value: str):
    try:
        return dateparser.parse(value)
    except Exception:
        return None

with links_file.open("r", encoding="utf-8") as fh:
    urls = [line.strip() for line in fh if line.strip()]

mode = (os.environ.get("MODO_TEXTOS") or "c").lower()
write_lock = Lock()

def process_url(url: str):
    downloaded = fetch_url(url)
    if not downloaded:
        return

    meta = metadata.extract_metadata(downloaded, default_url=url)
    title = meta.title if meta and meta.title else url.rsplit("/", 1)[-1]
    date_new = parse_date(meta.date) if meta and meta.date else None

    result = extract(downloaded, url=url, output_format="markdown", with_metadata=True)
    if not result:
        return

    fname_stem = slugify(title)[:100]
    out_path = dest_dir / f"{fname_stem}.md"

    with write_lock:
        if out_path.exists():
            if mode == "p":
                return
            existing = out_path.read_text(encoding="utf-8", errors="ignore")
            match = re.search(r"^date:\\s*(.+)$", existing, re.MULTILINE)
            date_old = parse_date(match.group(1)) if match else None

            if date_new and (date_old is None or date_new > date_old):
                out_path.write_text(result, encoding="utf-8")
            else:
                return
        else:
            out_path.write_text(result, encoding="utf-8")

with ThreadPoolExecutor(max_workers=8) as executor:
    futures = [executor.submit(process_url, url) for url in urls]
    for _ in as_completed(futures):
        pass
PY

    # --- PASSO 3: VÍDEOS (Suporta CDNs nativamente) ---
    echo " > [2/3] Baixando vídeos..."

    # 3a. Captura links diretos .mp4 embutidos nas páginas e URLs de players
    python3 - <<'PY' "$nome_pasta/Videos" "$nome_pasta/links_filtrados.txt"
import pathlib
import re
import sys
import requests

from trafilatura import fetch_url

dest_dir = pathlib.Path(sys.argv[1])
links_file = pathlib.Path(sys.argv[2])

dest_dir.mkdir(parents=True, exist_ok=True)
mp4_file = dest_dir / "links_mp4.txt"
ytdlp_file = dest_dir / "links_ytdlp.txt"
found_mp4 = set()
found_embed = set()
yt_ids = set()

with links_file.open("r", encoding="utf-8") as fh:
    urls = [line.strip() for line in fh if line.strip()]

for url in urls:
    # Se a URL já for um .mp4 direto, guarda e pula fetch pesado
    if re.search(r"\\.mp4($|[?#])", url, flags=re.IGNORECASE):
        found_mp4.add(url.split("#", 1)[0])
        continue

    # Tenta trafilatura; se falhar, usa requests com UA
    html = fetch_url(url)
    if not html:
        try:
            resp = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=15, allow_redirects=True)
            if resp.ok:
                html = resp.text
        except Exception:
            html = None

    if not html:
        continue
    # Links diretos .mp4 dentro da página
    for match in re.findall(r"https?://[^\"'\\s]+\\.mp4(?:\\?[^\"'\\s]*)?", html, flags=re.IGNORECASE):
        found_mp4.add(match.split("#", 1)[0])
    # Players embed (Wistia/Vimeo) e captura de YouTube em vários formatos
    for match in re.findall(r"https?://fast\\.wistia\\.net/embed/iframe/[\\w-]+[^\"'\\s]*", html, flags=re.IGNORECASE):
        found_embed.add(match.split("#", 1)[0].strip("'\""))
    for match in re.findall(r"https?://player\\.vimeo\\.com/video/\\d+[^\"'\\s]*", html, flags=re.IGNORECASE):
        found_embed.add(match.split("#", 1)[0].strip("'\""))

    # YouTube: embed, watch e thumbnails
    for yid in re.findall(r"(?:https?:)?//www\\.youtube\\.com/embed/([\\w-]+)", html, flags=re.IGNORECASE):
        yt_ids.add(yid)
    for yid in re.findall(r"https?://www\\.youtube\\.com/watch\\?v=([\\w-]+)", html, flags=re.IGNORECASE):
        yt_ids.add(yid)
    for thumb in re.findall(r"https?://i\\.ytimg\\.com/vi(?:_webp)?/([\\w-]+)/", html, flags=re.IGNORECASE):
        yt_ids.add(thumb)

    for yid in yt_ids:
        found_embed.add(f"https://www.youtube.com/watch?v={yid}")

if found_mp4:
    mp4_file.write_text("\n".join(sorted(found_mp4)), encoding="utf-8")
if found_embed:
    ytdlp_file.write_text("\n".join(sorted(found_embed)), encoding="utf-8")
PY

    # 3b. Baixa vídeos incorporados com links diretos .mp4 (se houver)
    if [ -s "$nome_pasta/Videos/links_mp4.txt" ]; then
        echo "   > Baixando .mp4 incorporados..."
        wget -i "$nome_pasta/Videos/links_mp4.txt" \
             --content-disposition --trust-server-names \
             --no-verbose --show-progress \
             -P "$nome_pasta/Videos"
    fi

    # 3c. Usa yt-dlp para players/embeds (Wistia/YouTube/Vimeo/etc.) encontrados
    if [ -s "$nome_pasta/Videos/links_ytdlp.txt" ]; then
        echo "   > Baixando players (Wistia/YT/Vimeo)..."
        yt-dlp -a "$nome_pasta/Videos/links_ytdlp.txt" \
               --paths "$nome_pasta/Videos" \
               -o "%(title)s [%(id)s].%(ext)s" \
               --download-archive "$nome_pasta/historico_videos.txt" \
               --ignore-errors --no-warnings \
               --format "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best"
    else
        echo "   > Nenhum embed de vídeo encontrado para yt-dlp."
    fi

    # Limpa listas temporárias de vídeo
    rm -f "$nome_pasta/Videos/links_mp4.txt" "$nome_pasta/Videos/links_ytdlp.txt"

    # --- PASSO 4: PDFS (apenas arquivos .pdf encontrados nas páginas) ---
    echo " > [3/3] Buscando PDF embutidos..."
    python3 - <<'PY' "$nome_pasta/PDFs" "$nome_pasta/links_filtrados.txt"
import pathlib
import re
import sys
from urllib.parse import urljoin

from trafilatura import fetch_url

dest_dir = pathlib.Path(sys.argv[1])
links_file = pathlib.Path(sys.argv[2])

dest_dir.mkdir(parents=True, exist_ok=True)
pdf_list = dest_dir / "links_pdfs.txt"
found = set()

with links_file.open("r", encoding="utf-8") as fh:
    urls = [line.strip() for line in fh if line.strip()]

pdf_pattern = re.compile(r"\\.pdf($|[?#])", re.IGNORECASE)

for page_url in urls:
    html = fetch_url(page_url)
    if not html:
        continue
    # Procura href com .pdf (suporta relativo)
    for match in re.findall(r'href=["\\\']([^"\\\']+)', html, flags=re.IGNORECASE):
        candidate = urljoin(page_url, match)
        clean = candidate.split("#", 1)[0]
        if pdf_pattern.search(clean):
            found.add(clean)

if found:
    pdf_list.write_text("\\n".join(sorted(found)), encoding="utf-8")
PY

    if [ -s "$nome_pasta/PDFs/links_pdfs.txt" ]; then
        wget -i "$nome_pasta/PDFs/links_pdfs.txt" \
             --content-disposition \
             --trust-server-names \
             --timestamping \
             --no-verbose --show-progress \
             -P "$nome_pasta/PDFs"
    else
        echo "   > Nenhum PDF encontrado."
    fi

    # Limpa lista temporária de PDFs
    rm -f "$nome_pasta/PDFs/links_pdfs.txt"

    # Remove pasta de PDFs se continuar vazia (nenhum .pdf baixado)
    if [ -d "$nome_pasta/PDFs" ]; then
        shopt -s nullglob
        pdfs=("$nome_pasta"/PDFs/*.pdf)
        if [ ${#pdfs[@]} -eq 0 ]; then
            rm -rf "$nome_pasta/PDFs"
        fi
        shopt -u nullglob
    fi

    if [ -f "$nome_pasta/links_filtrados.txt" ]; then
        rm "$nome_pasta/links_filtrados.txt"
    fi

    # Remove pastas vazias de textos e vídeos
    if [ -d "$nome_pasta/Textos" ]; then
        shopt -s nullglob
        mds=("$nome_pasta"/Textos/*.md)
        if [ ${#mds[@]} -eq 0 ]; then
            rm -rf "$nome_pasta/Textos"
        fi
        shopt -u nullglob
    fi
    if [ -d "$nome_pasta/Videos" ]; then
        shopt -s nullglob
        vids=("$nome_pasta"/Videos/*.mp4 "$nome_pasta"/Videos/*.mkv "$nome_pasta"/Videos/*.m4a "$nome_pasta"/Videos/*.webm)
        if [ ${#vids[@]} -eq 0 ]; then
            rm -rf "$nome_pasta/Videos"
        fi
        shopt -u nullglob
    fi

    echo "Concluído: $nome_pasta"
done

echo "--------------------------------------------------------"
echo "Finalizado."
