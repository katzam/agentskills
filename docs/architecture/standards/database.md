# Database Standards

## Purpose

Use these rules for schema, migration, and persistence changes. The goal is to keep database work source-controlled, verifiable, and aligned with application persistence assumptions.

## Canonical Artifacts

- `AGENTS.md`
- `docs/architecture/repo-map.md`
- the migration, schema, and verification surfaces documented in the repo map

## Rules

- Represent schema changes through source-controlled migration assets, not ad hoc DB mutation.
- Use one migration file per logical schema change when practical.
- Prefer forward-only, fail-closed migrations.
- Prefer expand/contract evolution when schema changes may impact runtime safety.
- Keep structural schema changes separate from backfills when practical.
- Verify DB changes with the repo's schema apply and verification commands documented in `AGENTS.md`.
- Keep application persistence assumptions aligned with any schema changes.
- Use `skills/project-database/references/memory.md` only for recurring, reusable lessons after a verified fix.

## Compliance Checklist

- A source-controlled migration asset exists for the schema change.
- No schema-only fix was applied outside the migration system as the durable solution.
- Verification evidence was captured.
- Application persistence assumptions were updated when needed.
