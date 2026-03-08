# Getting Started

Use this repository as a starter for a repo-local Codex workflow.

## Setup

1. Copy these files into the target application repository.
2. Update [docs/architecture/repo-map.md](docs/architecture/repo-map.md) so the skills know where frontend, backend, database, docs, and scripts actually live.
3. Replace the placeholder validation commands in [AGENTS.md](AGENTS.md) with real project commands.
4. Tighten the standards in:
   - [docs/architecture/standards/frontend-ui.md](docs/architecture/standards/frontend-ui.md)
   - [docs/architecture/standards/backend.md](docs/architecture/standards/backend.md)
   - [docs/architecture/standards/database.md](docs/architecture/standards/database.md)
5. Validate the skill set with `bash scripts/codex/validate-skills.sh`.

## Optional Requirement Mirror Flow

If your project keeps canonical requirement docs as `.docx` files:

1. Register them in [docs/requirements/source-manifest.md](docs/requirements/source-manifest.md).
2. Put the managed copies under `docs/requirements/source/docx/`.
3. Run `bash scripts/docs/extract-docx-to-markdown.sh`.

This generates searchable Markdown mirrors under `docs/requirements/source/markdown/`.

## Recommended First Customizations

- Replace `project-*` skill names with your app name if you want stronger repo identity.
- Add concrete examples to the standards docs.
- Add QA wrappers under `scripts/qa/` for your most important smoke flows.
- Add one real task brief under `tasks/open/` to prove the workflow.
