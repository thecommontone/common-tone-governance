#!/bin/bash
# corpus-harvest Stage 0 adapter: youtube.
# Capability-based execution: the URL is validated against a strict allowlist
# pattern and passed to yt-dlp as a single argv element — never interpolated
# into a shell string, never eval'd. Writes an acquisition receipt per run.
# Lineage: the 2026-08-24 12tone scrape (yt-dlp, archive file, fetch log),
# hardened. Usage: acquire_youtube.sh <staging_root> <channel_or_playlist_url>
set -euo pipefail

STAGING_ROOT="${1:?usage: acquire_youtube.sh <staging_root> <url>}"
URL="${2:?usage: acquire_youtube.sh <staging_root> <url>}"
YTDLP="${YTDLP_BIN:-yt-dlp}"
MIN_FREE_MB="${MIN_FREE_MB:-500}"

# --- validate staging root -------------------------------------------------
[ -f "$STAGING_ROOT/STATE.json" ] || { echo "REFUSED: $STAGING_ROOT has no STATE.json (scaffold first)" >&2; exit 1; }
RAW="$STAGING_ROOT/RAW"
mkdir -p "$RAW" "$RAW/_RECEIPTS"

# --- validate URL (strict allowlist; anything else is refused) -------------
# Allowed: https://www.youtube.com/@handle | /channel/UC<22> | /c/name | /playlist?list=ID
if ! printf '%s' "$URL" | grep -Eq '^https://(www\.)?youtube\.com/(@[A-Za-z0-9._-]+|channel/UC[A-Za-z0-9_-]{22}|c/[A-Za-z0-9._-]+|playlist\?list=[A-Za-z0-9_-]+)$'; then
  echo "REFUSED: URL fails the youtube allowlist pattern: $URL" >&2
  exit 1
fi

# --- dependency + disk checks ---------------------------------------------
command -v "$YTDLP" >/dev/null 2>&1 || { echo "REFUSED: yt-dlp not found ($YTDLP)" >&2; exit 1; }
TOOL_VERSION="$("$YTDLP" --version 2>/dev/null | head -1 || echo unknown)"
FREE_MB=$(df -Pm "$STAGING_ROOT" | awk 'NR==2{print $4}')
[ "$FREE_MB" -ge "$MIN_FREE_MB" ] || { echo "REFUSED: only ${FREE_MB}MB free (< ${MIN_FREE_MB}MB)" >&2; exit 1; }

# --- fixed command shape; URL is one argv element --------------------------
ARCHIVE="$RAW/_fetch_archive.txt"
LOG="$RAW/_fetch_log.txt"
ACQUIRED_AT="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
"$YTDLP" \
  --skip-download \
  --write-subs --write-auto-subs --sub-langs en \
  --download-archive "$ARCHIVE" \
  --output "%(upload_date)s_%(id)s_%(title)s.%(ext)s" \
  --paths "$RAW" \
  --no-overwrites \
  "$URL" >>"$LOG" 2>&1 || { echo "yt-dlp failed — see $LOG" >&2; exit 1; }

# --- receipt: every new file hashed ---------------------------------------
python3 - "$STAGING_ROOT" "$URL" "$TOOL_VERSION" "$ACQUIRED_AT" <<'PYEOF'
import hashlib, json, os, re, sys
root, url, tool_version, acquired_at = sys.argv[1:5]
raw = os.path.join(root, "RAW")
receipts_dir = os.path.join(raw, "_RECEIPTS")
existing = set()
for fn in os.listdir(receipts_dir):
    if fn.endswith(".json"):
        with open(os.path.join(receipts_dir, fn), encoding="utf-8") as f:
            for entry in json.load(f).get("files", []):
                existing.add(entry["path"])
fname = re.compile(r"^(\d{8})_([A-Za-z0-9_-]{11})_")
new_files = []
for fn in sorted(os.listdir(raw)):
    p = os.path.join(raw, fn)
    rel = os.path.join("RAW", fn)
    if not os.path.isfile(p) or fn.startswith("_") or rel in existing:
        continue
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for block in iter(lambda: f.read(65536), b""):
            h.update(block)
    m = fname.match(fn)
    item_id = m.group(2) if m else os.path.splitext(fn)[0]
    published = f"{m.group(1)[:4]}-{m.group(1)[4:6]}-{m.group(1)[6:]}" if m else None
    new_files.append((item_id, published, {"path": rel, "sha256": h.hexdigest(),
                                           "bytes": os.path.getsize(p)}))
if not new_files:
    print("no new files acquired (archive up to date)")
    sys.exit(0)
by_item = {}
for item_id, published, entry in new_files:
    by_item.setdefault((item_id, published), []).append(entry)
n = 0
for (item_id, published), files in sorted(by_item.items()):
    receipt = {"item_id": item_id, "adapter": "youtube", "source_locator": url,
               "source_url": f"https://www.youtube.com/watch?v={item_id}"
                             if len(item_id) == 11 else None,
               "published_at": published, "acquired_at": acquired_at,
               "tool": {"name": "yt-dlp", "version": tool_version},
               "files": files, "notes": None}
    out = os.path.join(receipts_dir, f"{item_id}.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(receipt, f, indent=2)
    n += 1
print(f"receipts written: {n} item(s)")
PYEOF
echo "acquire complete: $URL -> $RAW"
