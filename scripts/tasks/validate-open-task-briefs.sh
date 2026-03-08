#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/../.." && pwd)"

usage() {
  cat <<'EOF'
Usage: bash scripts/tasks/validate-open-task-briefs.sh [task-brief-path ...]

Fails if any checked task brief still has non-empty content under `## Open Questions`.

Defaults to all files under `tasks/open/*.md` when no paths are provided.
EOF
}

fail() {
  echo "[validate-open-task-briefs] $*" >&2
  exit 1
}

has_unresolved_open_questions() {
  local file="$1"

  awk '
    BEGIN {
      in_section = 0
      unresolved = 0
    }
    /^## Open Questions[[:space:]]*$/ {
      in_section = 1
      next
    }
    in_section && /^##[[:space:]]/ {
      in_section = 0
    }
    in_section {
      if ($0 ~ /^[[:space:]]*$/) {
        next
      }
      if ($0 ~ /^[[:space:]]*<!--.*-->[[:space:]]*$/) {
        next
      }
      unresolved = 1
      print $0
    }
    END {
      exit unresolved ? 0 : 1
    }
  ' "$file"
}

declare -a FILES=()

if [[ $# -gt 0 ]]; then
  case "$1" in
    --help|-h)
      usage
      exit 0
      ;;
  esac
fi

if [[ $# -eq 0 ]]; then
  while IFS= read -r file; do
    FILES+=("$file")
  done < <(find "${REPO_ROOT}/tasks/open" -maxdepth 1 -type f -name '*.md' | sort)
else
  for path in "$@"; do
    if [[ "${path}" != /* ]]; then
      FILES+=("${REPO_ROOT}/${path}")
    else
      FILES+=("${path}")
    fi
  done
fi

if [[ ${#FILES[@]} -eq 0 ]]; then
  echo "[validate-open-task-briefs] No open task briefs found."
  exit 0
fi

status=0

for file in "${FILES[@]}"; do
  [[ -f "${file}" ]] || fail "Task brief not found: ${file}"

  if output="$(has_unresolved_open_questions "${file}")"; then
    echo "[validate-open-task-briefs] FAIL ${file}" >&2
    echo "${output}" >&2
    status=1
    continue
  fi

  echo "[validate-open-task-briefs] PASS ${file}"
done

exit "${status}"

