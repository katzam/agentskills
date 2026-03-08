# Agent Skills Framework

This repository is a genericized starter extracted from the Ankora project.

It keeps the useful parts of that setup:

- one main Codex agent
- repo-local skills under `skills/`
- durable task briefs under `tasks/`
- lightweight docs that explain the workflow
- simple validation scripts for skills and task briefs

The goal is to give another app repo a small, repeatable framework for AI-assisted development without turning the repo into a workflow engine.

## What Is Included

- `AGENTS.md`: repo operating notes and guardrails
- `docs/`: framework docs, standards templates, and requirement-source guidance
- `skills/`: generic architect, frontend, backend, database, docs, QA, and review skills
- `tasks/`: durable task-brief structure and template
- `scripts/codex/`: skill validation helpers
- `scripts/tasks/`: task-brief readiness check
- `scripts/docs/`: optional DOCX-to-Markdown requirement mirror helper

## How To Use This In Another App

1. Copy this structure into the target application repo.
2. Update [docs/architecture/repo-map.md](docs/architecture/repo-map.md) with the real code layout.
3. Replace the placeholder validation commands in [AGENTS.md](AGENTS.md).
4. Customize the standards under [docs/architecture/standards](docs/architecture/standards).
5. Rename `project-*` skills if you want app-specific names.
6. Run `bash scripts/codex/validate-skills.sh`.

## Design Rules

- Skills are repo-local guidance, not separate workers.
- The main Codex agent stays responsible for the task from start to finish.
- Task briefs are the durable source for implementation-ready work.
- Standards docs stay canonical; skills should point to them instead of duplicating them.
- Keep the framework small enough that another app can adopt it quickly.
