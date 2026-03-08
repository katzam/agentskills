---
name: project-frontend
description: Frontend implementation guidance for this project. Use when changing routes, layouts, screens, components, hooks, theming, localization, or the centralized HTTP boundary.
---

Work within the project's frontend patterns.

1. Read:
- `AGENTS.md`
- `docs/architecture/repo-map.md`
- `docs/architecture/standards/frontend-ui.md`
- `references/memory.md`

When a task brief under `tasks/open/*` or `tasks/completed/*` is provided, read it before coding and treat it as the implementation anchor alongside repo standards.

2. Preserve frontend guardrails:
- keep HTTP calls inside the repo's intended API boundary
- preserve the existing app structure, theme inheritance, and visual language unless the task explicitly changes design direction
- reuse shared UI artifacts before creating new ones

3. Keep new UI inside the existing theme and layout systems documented in `docs/architecture/repo-map.md`.

4. If backend changes are relevant, call out:
- API request or response shape dependencies
- loading, error, and empty-state impacts
- any required boundary updates on the frontend side

5. Default validation:
- run the frontend validation commands documented in `AGENTS.md`

6. Do not create workflow artifacts, mock handoff contracts, or design-breaking hardcoded implementations.
