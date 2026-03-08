#!/usr/bin/env bash

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
MANIFEST_PATH="$REPO_ROOT/docs/requirements/source-manifest.md"
OUTPUT_ROOT="$REPO_ROOT/docs/requirements/source/markdown"

PANDOC_BIN="$(command -v pandoc || true)"
TEXTUTIL_BIN="$(command -v textutil || true)"

if [[ ! -f "$MANIFEST_PATH" ]]; then
  echo "Missing manifest: $MANIFEST_PATH" >&2
  exit 1
fi

if [[ -z "$PANDOC_BIN" && -z "$TEXTUTIL_BIN" ]]; then
  echo "Neither pandoc nor textutil is available for DOCX extraction." >&2
  exit 1
fi

manifest_rows() {
  awk -F'\\|' '
    /^## Canonical `.docx` Sources/ {
      in_table = 1
      next
    }
    /^## / && in_table {
      exit
    }
    in_table {
      current = $2
      planned = $6
      gsub(/^[[:space:]]*`/, "", current)
      gsub(/`[[:space:]]*$/, "", current)
      gsub(/^[[:space:]]*`/, "", planned)
      gsub(/`[[:space:]]*$/, "", planned)
      if (current ~ /^docs\/.*\.docx$/ && planned ~ /^docs\/requirements\/source\/docx\/.*\.docx$/) {
        print current "\t" planned
      }
    }
  ' "$MANIFEST_PATH"
}

render_markdown() {
  local source_path="$1"

  if [[ -n "$PANDOC_BIN" ]]; then
    "$PANDOC_BIN" "$source_path" --to=gfm --wrap=none
    return
  fi

  "$TEXTUTIL_BIN" -convert txt -stdout "$source_path"
}

mkdir -p "$OUTPUT_ROOT"
find "$OUTPUT_ROOT" -type f -name '*.md' ! -name 'README.md' -delete

generated_count=0

while IFS=$'\t' read -r source_rel planned_rel; do
  [[ -n "$source_rel" ]] || continue

  source_abs="$REPO_ROOT/$source_rel"
  if [[ ! -f "$source_abs" ]]; then
    echo "Missing canonical source: $source_rel" >&2
    exit 1
  fi

  output_rel="$(printf '%s' "$planned_rel" | sed 's#/docx/#/markdown/#; s/\.docx$/.md/')"
  output_abs="$REPO_ROOT/$output_rel"
  output_dir="$(dirname "$output_abs")"
  temp_file="$(mktemp)"

  mkdir -p "$output_dir"
  render_markdown "$source_abs" > "$temp_file"

  {
    printf '<!-- Generated from `%s` by `bash scripts/docs/extract-docx-to-markdown.sh`. Do not edit directly. -->\n\n' "$source_rel"
    cat "$temp_file"
    printf '\n'
  } > "$output_abs"

  rm -f "$temp_file"
  generated_count=$((generated_count + 1))
  printf 'Wrote %s\n' "$output_rel"
done < <(manifest_rows)

find "$OUTPUT_ROOT" -mindepth 1 -type d -empty -delete

if [[ "$generated_count" -eq 0 ]]; then
  echo "No canonical DOCX sources were found in $MANIFEST_PATH" >&2
  exit 1
fi

printf 'Generated %d Markdown mirrors under %s\n' "$generated_count" "$OUTPUT_ROOT"

