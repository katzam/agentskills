#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/../.." && pwd)"
FALLBACK_VALIDATOR="${SCRIPT_DIR}/fallback_validate_skill.py"
EXTERNAL_VALIDATOR="${HOME}/.codex/skills/.system/skill-creator/scripts/quick_validate.py"

if [[ ! -f "${FALLBACK_VALIDATOR}" ]]; then
  echo "Repo skill validator not found: ${FALLBACK_VALIDATOR}" >&2
  exit 1
fi

if ! command -v python3 >/dev/null 2>&1; then
  echo "python3 is required to validate skills." >&2
  exit 1
fi

declare -a EXTRA_VALIDATORS=()
if [[ -f "${EXTERNAL_VALIDATOR}" ]] && python3 -c "import yaml" >/dev/null 2>&1; then
  EXTRA_VALIDATORS+=("${EXTERNAL_VALIDATOR}")
fi

mapfile -t SKILLS < <(find "${REPO_ROOT}/skills" -mindepth 1 -maxdepth 1 -type d | sort)

if [[ "${#SKILLS[@]}" -eq 0 ]]; then
  echo "No repo skills found under ${REPO_ROOT}/skills" >&2
  exit 1
fi

failed=0
for skill_path in "${SKILLS[@]}"; do
  skill_name="$(basename "${skill_path}")"
  if ! python3 "${FALLBACK_VALIDATOR}" "${skill_path}"; then
    echo "[validate-skills] FAIL ${skill_name}" >&2
    failed=1
    continue
  fi

  extra_failed=0
  for validator in "${EXTRA_VALIDATORS[@]}"; do
    if ! python3 "${validator}" "${skill_path}" >/dev/null; then
      echo "[validate-skills] FAIL ${skill_name} (external validator: ${validator})" >&2
      extra_failed=1
      break
    fi
  done

  if [[ ${extra_failed} -eq 0 ]]; then
    echo "[validate-skills] PASS ${skill_name}"
  else
    failed=1
  fi
done

exit "${failed}"

