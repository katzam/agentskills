---
name: project-architect
description: Repo-specific planning and impact analysis for this project. Use when a task spans multiple domains, the right files are unclear, API, UI, and data changes must be coordinated, requirement sources must be traced, or the agent needs to decide what frontend, backend, database, docs, scripts, or skill work is required before implementation.
---

Ground the task in the repo before proposing changes.

1. Read the canonical repo guidance:
- `AGENTS.md`
- `docs/README.md`
- `docs/architecture/repo-map.md`
- `references/memory.md`

If the task affects the framework itself, also read `docs/architecture/codex-skill-framework.md`.
When a task needs requirement-source text, prefer `docs/requirements/source/markdown/*` for search and read, then use `docs/requirements/source-manifest.md` to trace back to canonical source files when needed.
When a task brief path under `tasks/open/*` or `tasks/completed/*` is provided, read it before producing new analysis.

2. Identify the impacted domains:
- `frontend`
- `backend`
- `database`
- `docs`
- `scripts`
- `skills`
- `tasks`

3. Read the relevant standards docs for each impacted implementation domain:
- `docs/architecture/standards/frontend-ui.md`
- `docs/architecture/standards/backend.md`
- `docs/architecture/standards/database.md`

4. Produce a short working analysis:
- relevant files and likely entrypoints
- impacted interfaces or contracts
- required validations by domain
- assumptions that should be locked before implementation

If the active task brief under `tasks/open/*` still has unresolved items in `## Open Questions`, treat the task as not ready for development. Close those questions first by getting answers, converting them into explicit decisions in the brief, or marking them as deferred follow-ups that are clearly out of scope for the implementation slice. Use `bash scripts/tasks/validate-open-task-briefs.sh <task-brief-path>` when you need a mechanical readiness check.

When the user asks for a durable implementation brief, draft or refine `tasks/open/<task-id>.md` using `tasks/templates/task-brief-template.md`.
Task briefs should combine current codebase findings, requirement sources consulted, dependencies, acceptance criteria, persistence considerations, validation expectations, and explicit verification rules that define how to tell whether the feature works.
When writing verification rules, prefer concrete pass or fail statements plus the most direct UI, API, and data checks a later QA run can execute without reinterpretation.

5. For analysis-heavy or high-risk tasks, write a reasoning certificate using `references/reasoning-certificate.md`.

6. Do not create workflow graphs, handoff schemas, planner artifacts, or skill-to-skill payload contracts. Keep durable briefs in `tasks/*` and temporary notes in untracked `handoffs/*`.

7. Keep output compact and implementation-oriented. The goal is to help the main agent move into coding quickly.
