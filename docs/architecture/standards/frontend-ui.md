# Frontend UI Standards

## Purpose

Use these rules for client-side UI changes. The goal is to keep frontend behavior aligned with the app's existing component library, theme system, layout system, and HTTP boundary.

## Canonical Artifacts

- `AGENTS.md`
- `docs/architecture/repo-map.md`
- the shared UI, theme, and API-boundary surfaces documented in the repo map

## Rules

- Reuse an existing shared primitive before creating a new interaction container, form control, or feedback surface.
- Keep new UI inside the active theme and layout systems so project-wide styling still applies automatically.
- Prefer the repo's centralized HTTP boundary over direct request calls from components.
- Avoid hardcoded theme values when tokens or shared styles already exist.
- Preserve the existing visual language unless the task explicitly changes design direction.
- Reuse existing confirmation, error, loading, and success patterns before inventing new ones.
- Keep changes scoped to the relevant feature area and only touch shared layers when needed.
- If frontend work depends on backend changes, surface the request, response, validation, and error-state implications clearly.

## Compliance Checklist

- Reused an existing primitive where appropriate.
- No new hardcoded styling breaks theme inheritance.
- API traffic stayed inside the repo's intended HTTP boundary.
- Loading, error, and empty states are handled consistently.
- Frontend validations documented in `AGENTS.md` were run.

