# Repository Architecture Map

Use this file to describe the real structure of the target application repository.

Replace the placeholders below with concrete paths before relying on the framework.

## Runtime Packaging
- Final deployable artifact: `<replace-with-runtime-artifact>`
- UI entrypoint or served path: `<replace-with-ui-runtime-surface>`
- API entrypoint or served path: `<replace-with-api-runtime-surface>`

## Frontend
- App bootstrap: `<replace-with-frontend-entrypoints>`
- Routing: `<replace-with-router-paths>`
- API boundary: `<replace-with-central-http-surface>`
- Shared UI: `<replace-with-shared-ui-paths>`
- Theme or design system: `<replace-with-theme-paths>`

## Backend
- Application entrypoint: `<replace-with-backend-entrypoint>`
- HTTP layer: `<replace-with-controller-paths>`
- Auth and session core: `<replace-with-auth-paths>`
- Persistence models: `<replace-with-model-paths>`
- Data access: `<replace-with-repository-paths>`
- Tests: `<replace-with-backend-test-paths>`

## Database And Schema Assets
- Migration directory: `<replace-with-migration-paths>`
- Canonical schema or reference assets: `<replace-with-schema-paths>`
- Seed or fixture data: `<replace-with-seed-paths>`

## Scripts
- Codex skill helpers: `scripts/codex/*`
- Task helpers: `scripts/tasks/*`
- Docs helpers: `scripts/docs/*`
- Runtime, database, or QA wrappers: `<replace-with-app-specific-script-paths>`

## Documentation Ownership
- Requirement sources and manifest: `docs/requirements/*`
- Searchable requirement mirrors: `docs/requirements/source/markdown/*`
- Architecture reference docs: `docs/architecture/*`
- Task briefs: `tasks/*`
- Repository operating notes: `AGENTS.md`

