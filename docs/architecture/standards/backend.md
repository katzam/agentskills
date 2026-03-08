# Backend Standards

## Purpose

Use these rules for backend and API changes. The goal is to keep backend behavior aligned with the project's existing structure, validation patterns, authorization rules, and API contracts.

## Canonical Artifacts

- `AGENTS.md`
- `docs/architecture/repo-map.md`
- the backend entrypoints, auth surfaces, DTO patterns, and error abstractions documented in the repo map

## Rules

- Follow the project's established validation and authorization patterns instead of inventing new ones per endpoint.
- Preserve a consistent error response shape across the backend.
- Prefer existing response envelopes, DTO patterns, and exception handling conventions.
- Public or low-auth endpoints should be rate-limited and should avoid leaking identity state when that matters.
- Keep model identity, equality, serialization, and persistence assumptions aligned with current repo conventions.
- Check source-controlled schema or migration assets before changing persistence models.
- Prefer explicit constructor injection for runtime-managed classes.
- Surface endpoint, payload, validation, or authorization impacts when backend changes affect other domains.
- Keep changes minimal within the current package and module structure unless the task explicitly includes refactoring.

## Compliance Checklist

- Error contract is preserved.
- No custom response-shape drift was introduced.
- Validation and auth follow the existing project patterns.
- Persistence model changes were checked against source-controlled schema assets.
- Backend validations documented in `AGENTS.md` were run.

