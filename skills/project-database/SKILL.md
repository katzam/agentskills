---
name: project-database
description: Database and schema guidance for this project. Use when a task changes database structure, migrations, schema verification, persistence contracts, or DB-related application behavior that must stay aligned with schema assets.
---

Work within the project's database rules.

1. Read:
- `AGENTS.md`
- `docs/architecture/repo-map.md`
- `docs/architecture/standards/database.md`
- `references/memory.md`

When a task brief under `tasks/open/*` or `tasks/completed/*` exists, use it as the primary persistence-planning input.

2. Preserve database guardrails:
- use source-controlled migrations
- fail closed on migration errors
- do not rely on ad hoc DB mutation as the durable solution
- schema work must be represented through migration assets plus verification evidence

3. Use the database and migration surfaces documented in `docs/architecture/repo-map.md` as the default place to inspect or edit persistence assets.

4. When schema changes affect application code, surface:
- impacted models, entities, or repositories
- changed assumptions in DTOs, services, or API behavior
- required verification steps

During the requirements or task-brief phase, review and refine the `Persistence Considerations` section of `tasks/open/<task-id>.md`.
Capture likely tables or entities, lifecycle and audit needs, uniqueness or expiry constraints, and open schema questions.
Do not start migrations or lock schema design during the task-brief phase unless the user explicitly moves into implementation.

5. If DB apply or verify fails:
- inspect the command output and any report file
- correct the migration or schema issue
- rerun verification
- update `references/memory.md` only if the lesson is reusable and the fix is confirmed

6. Default validation:
- run the database verification commands documented in `AGENTS.md`
- run backend tests if persistence behavior changed

7. Do not introduce orchestration contracts, generated task-state artifacts, or raw run logs as durable memory. Put durable persistence-planning notes in `tasks/*`, not in `handoffs/*` or `references/memory.md`.
