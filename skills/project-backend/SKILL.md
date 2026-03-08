---
name: project-backend
description: Backend implementation guidance for this project. Use when changing backend services, controllers, auth, repositories, DTOs, persistence models, backend configuration, backend tests, or API response behavior.
---

Work within the project's backend patterns.

1. Read:
- `AGENTS.md`
- `docs/architecture/repo-map.md`
- `docs/architecture/standards/backend.md`
- `references/memory.md`

When a task brief under `tasks/open/*` or `tasks/completed/*` is provided, read it before coding and treat it as the implementation anchor alongside repo standards.

2. Preserve backend guardrails:
- keep error responses aligned with the project's standard backend contract
- keep model, serialization, auth, and persistence rules aligned with the conventions documented in the repo
- prefer existing exception, DTO, and authorization patterns over new one-off conventions

3. Prefer minimal changes aligned with the existing package, module, and layering structure described in `docs/architecture/repo-map.md`.

4. When backend changes affect other domains, surface:
- endpoint or payload changes
- validation or auth behavior changes
- error-contract impacts
- migration or persistence dependencies

5. Default validation:
- run the backend validation commands documented in `AGENTS.md`

6. Do not invent orchestration artifacts, role handoff payloads, or custom backend conventions that bypass repo standards.
