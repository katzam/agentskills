#!/usr/bin/env python3
"""
Minimal skill validator that does not require PyYAML.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

MAX_SKILL_NAME_LENGTH = 64
ALLOWED_PROPERTIES = {"name", "description", "license", "allowed-tools", "metadata"}
REQUIRED_AGENT_INTERFACE_KEYS = ("display_name", "short_description", "default_prompt")
PATH_TOKEN_PATTERN = re.compile(r"(?<![\w.-])([A-Za-z0-9_.-]+(?:/[A-Za-z0-9_.*-]+)+)(?![\w.-])")
CODE_SPAN_PATTERN = re.compile(r"`([^`]+)`")
VALIDATED_PATH_ROOTS = {
    "agents",
    "assets",
    "backend",
    "database",
    "docs",
    "env",
    "frontend",
    "references",
    "scripts",
    "skills",
    "tasks",
    "templates",
}


def _strip_quotes(value: str) -> str:
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value


def _coerce_yaml_scalar(value: str) -> object:
    stripped = _strip_quotes(value.strip())
    if stripped == "true":
        return True
    if stripped == "false":
        return False
    return stripped


def parse_frontmatter(frontmatter_text: str) -> dict[str, object]:
    frontmatter: dict[str, object] = {}
    current_key: str | None = None

    for raw_line in frontmatter_text.splitlines():
        if not raw_line.strip() or raw_line.lstrip().startswith("#"):
            continue

        if raw_line.startswith((" ", "\t")):
            if current_key is None:
                raise ValueError("Indented content without a parent key")
            if frontmatter[current_key] is None:
                frontmatter[current_key] = []
            if not isinstance(frontmatter[current_key], list):
                raise ValueError(f"Unexpected nested content for key '{current_key}'")
            frontmatter[current_key].append(raw_line.strip())
            continue

        if ":" not in raw_line:
            raise ValueError(f"Invalid frontmatter line: {raw_line}")

        key, value = raw_line.split(":", 1)
        key = key.strip()
        value = value.strip()
        current_key = key

        if not key:
            raise ValueError("Empty frontmatter key")

        if value:
            frontmatter[key] = _strip_quotes(value)
        else:
            frontmatter[key] = None

    return frontmatter


def parse_agent_yaml(agent_text: str) -> dict[str, dict[str, object]]:
    parsed: dict[str, dict[str, object]] = {}
    current_section: str | None = None

    for raw_line in agent_text.splitlines():
        if not raw_line.strip() or raw_line.lstrip().startswith("#"):
            continue

        indent = len(raw_line) - len(raw_line.lstrip(" "))
        stripped = raw_line.strip()

        if indent == 0:
            if not stripped.endswith(":"):
                raise ValueError(f"Invalid top-level YAML line: {raw_line}")
            current_section = stripped[:-1].strip()
            if not current_section:
                raise ValueError("Empty top-level YAML section name")
            parsed[current_section] = {}
            continue

        if indent != 2:
            raise ValueError(f"Unsupported YAML indentation: {raw_line}")

        if current_section is None:
            raise ValueError("Nested YAML entry without a top-level section")

        if ":" not in stripped:
            raise ValueError(f"Invalid nested YAML line: {raw_line}")

        key, value = stripped.split(":", 1)
        key = key.strip()
        value = value.strip()
        if not key or not value:
            raise ValueError(f"Invalid nested YAML line: {raw_line}")

        parsed[current_section][key] = _coerce_yaml_scalar(value)

    return parsed


def extract_path_tokens(skill_body: str) -> set[str]:
    path_tokens: set[str] = set()
    for code_span in CODE_SPAN_PATTERN.findall(skill_body):
        for match in PATH_TOKEN_PATTERN.findall(code_span):
            path_tokens.add(match.rstrip(".,:"))
    return path_tokens


def reference_exists(base_dir: Path, token: str) -> bool:
    if "*" in token:
        prefix = token.split("*", 1)[0].rstrip("/")
        return bool(prefix) and (base_dir / prefix).exists()
    return (base_dir / token).exists()


def should_validate_reference(token: str) -> bool:
    first_segment = token.split("/", 1)[0]
    return first_segment in VALIDATED_PATH_ROOTS


def validate_skill(skill_path: str) -> tuple[bool, str]:
    skill_dir = Path(skill_path)
    skill_md = skill_dir / "SKILL.md"
    repo_root = skill_dir.parent.parent
    errors: list[str] = []

    if not skill_md.exists():
        return False, "SKILL.md not found"

    content = skill_md.read_text()
    if not content.startswith("---"):
        return False, "No YAML frontmatter found"

    match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not match:
        return False, "Invalid frontmatter format"

    try:
        frontmatter = parse_frontmatter(match.group(1))
    except ValueError as exc:
        return False, f"Invalid frontmatter: {exc}"

    unexpected_keys = set(frontmatter.keys()) - ALLOWED_PROPERTIES
    if unexpected_keys:
        allowed = ", ".join(sorted(ALLOWED_PROPERTIES))
        unexpected = ", ".join(sorted(unexpected_keys))
        return (
            False,
            f"Unexpected key(s) in SKILL.md frontmatter: {unexpected}. Allowed properties are: {allowed}",
        )

    if "name" not in frontmatter:
        return False, "Missing 'name' in frontmatter"
    if "description" not in frontmatter:
        return False, "Missing 'description' in frontmatter"

    name = frontmatter.get("name")
    if not isinstance(name, str):
        return False, f"Name must be a string, got {type(name).__name__}"
    name = name.strip()
    if name:
        if not re.match(r"^[a-z0-9-]+$", name):
            return (
                False,
                f"Name '{name}' should be hyphen-case (lowercase letters, digits, and hyphens only)",
            )
        if name.startswith("-") or name.endswith("-") or "--" in name:
            return (
                False,
                f"Name '{name}' cannot start or end with hyphen or contain consecutive hyphens",
            )
        if len(name) > MAX_SKILL_NAME_LENGTH:
            return (
                False,
                f"Name is too long ({len(name)} characters). Maximum is {MAX_SKILL_NAME_LENGTH} characters.",
            )

    description = frontmatter.get("description")
    if not isinstance(description, str):
        return False, f"Description must be a string, got {type(description).__name__}"
    description = description.strip()
    if description:
        if "<" in description or ">" in description:
            return False, "Description cannot contain angle brackets (< or >)"
        if len(description) > 1024:
            return (
                False,
                f"Description is too long ({len(description)} characters). Maximum is 1024 characters.",
            )

    if name != skill_dir.name:
        errors.append(
            f"Frontmatter name '{name}' does not match skill directory '{skill_dir.name}'"
        )

    agent_yaml = skill_dir / "agents" / "openai.yaml"
    if not agent_yaml.exists():
        errors.append("agents/openai.yaml not found")
    else:
        try:
            agent_config = parse_agent_yaml(agent_yaml.read_text())
        except ValueError as exc:
            errors.append(f"Invalid agents/openai.yaml: {exc}")
        else:
            interface = agent_config.get("interface")
            if not isinstance(interface, dict):
                errors.append("agents/openai.yaml is missing the 'interface' section")
            else:
                for key in REQUIRED_AGENT_INTERFACE_KEYS:
                    value = interface.get(key)
                    if not isinstance(value, str) or not value.strip():
                        errors.append(f"agents/openai.yaml is missing interface.{key}")

            policy = agent_config.get("policy")
            if not isinstance(policy, dict):
                errors.append("agents/openai.yaml is missing the 'policy' section")
            else:
                allow_implicit = policy.get("allow_implicit_invocation")
                if not isinstance(allow_implicit, bool):
                    errors.append(
                        "agents/openai.yaml must set policy.allow_implicit_invocation to true or false"
                    )

    body = content[match.end() :].strip()
    for token in sorted(extract_path_tokens(body)):
        if not should_validate_reference(token):
            continue
        if reference_exists(skill_dir, token) or reference_exists(repo_root, token):
            continue
        errors.append(f"Referenced path not found: {token}")

    if errors:
        return False, "; ".join(errors)

    return True, "Skill is valid!"


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python fallback_validate_skill.py <skill_directory>")
        sys.exit(1)

    valid, message = validate_skill(sys.argv[1])
    print(message)
    sys.exit(0 if valid else 1)

