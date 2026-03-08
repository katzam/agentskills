# Documentation Index

## Purpose
This index defines where canonical engineering, requirements, and workflow context lives for the framework.

## Canonical Sections
- Getting started: [GETTING_STARTED.md](../GETTING_STARTED.md)
- Requirement sources and mirrors: [docs/requirements/source-manifest.md](requirements/source-manifest.md)
- Searchable requirement mirrors: `docs/requirements/source/markdown/*`
- Durable task briefs: `tasks/open/*` and `tasks/completed/*`
- Plain-language development workflow: [docs/agent-skill-task-guide.md](agent-skill-task-guide.md)
- Architecture and code ownership: [docs/architecture/repo-map.md](architecture/repo-map.md)
- Codex skill framework: [docs/architecture/codex-skill-framework.md](architecture/codex-skill-framework.md)
- Coding standards: `docs/architecture/standards/*`
- Repository operating notes: [AGENTS.md](../AGENTS.md)

## Working Rules
1. Treat canonical requirement-source files as immutable inputs unless a task explicitly updates them.
2. Add new derived docs under a clearly named subdirectory and keep traceability explicit.
3. When requirement text needs to be searched or quoted, prefer `docs/requirements/source/markdown/*`.
4. Store durable implementation briefs under `tasks/*`, not under `docs/*`.
5. Keep standards docs canonical and let skills point to them instead of repeating them.
