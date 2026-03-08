---
name: project-docs
description: Documentation and requirement-traceability guidance for this project. Use when a task changes repo operating notes, architecture docs, standards docs, manifests, task briefs, or other project documentation that must stay aligned with implementation.
---

Keep project documentation accurate, canonical, and minimal.

1. Read:
- `docs/README.md`
- `docs/requirements/source-manifest.md`
- `docs/architecture/repo-map.md`
- `docs/architecture/codex-skill-framework.md`
- `AGENTS.md`
- `references/memory.md`
- `tasks/README.md` when the task involves creating or updating a task brief

When a task needs requirement-source text, prefer `docs/requirements/source/markdown/*` for search and read and use `docs/requirements/source-manifest.md` to trace back to the canonical source file when needed.

2. Treat requirement-source files in `docs/` as immutable inputs unless the task explicitly updates them.

3. When adding or changing derived docs:
- place them under a clear docs subdirectory
- keep traceability explicit
- update `docs/requirements/source-manifest.md` when required by repo policy

When the user asks for a durable implementation brief, create or refine `tasks/open/<task-id>.md` from repo context and requirement sources using `tasks/templates/task-brief-template.md`.
Treat `tasks/*` as committed task-brief artifacts, not as canonical requirement sources and not as temporary scratchpads.
After a feature is confirmed by review plus QA, use `project-docs` to sync backlog or tracking artifacts that changed state, such as `feature_tasks.md`, and to move the task brief from `tasks/open/*` to `tasks/completed/*` when the task is truly done.

4. Keep canonical standards in `docs/architecture/standards/*`.

5. Do not duplicate standards or workflow rules inside multiple docs or skills when a single canonical source can be updated.

6. Check for dead references after edits, including any new or updated links between `docs/*` and `tasks/*`.
