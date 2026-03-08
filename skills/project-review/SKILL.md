---
name: project-review
description: Final verification and risk review for project tasks. Use near completion to confirm acceptance criteria, required validations, residual risks, standards compliance, documentation alignment, and whether cross-domain changes are coherent before handoff.
---

Review project changes with a coding-focused mindset.

1. Read the task context, changed files, required domain validations, and the relevant standards docs for each impacted domain.
When acceptance criteria depend on requirement-source text, prefer `docs/requirements/source/markdown/*` and trace back to the canonical source via `docs/requirements/source-manifest.md`.
When a task brief exists under `tasks/open/*` or `tasks/completed/*`, use it as the primary acceptance-criteria reference.
If the brief still has unresolved items in `## Open Questions`, call that out as a process failure and do not treat the implementation as fully ready for completion until those questions are resolved or explicitly converted into deferred follow-ups.

2. Prioritize findings:
- bugs
- regressions
- contract mismatches
- missing validations
- stale docs or references
- drift from frontend, backend, or database standards

3. For analysis-heavy review claims, produce a reasoning certificate using `references/reasoning-certificate.md`.

4. Confirm domain checks match the changed surfaces using the validation commands documented in `AGENTS.md`.

5. Read `references/memory.md` for recurring review lessons. For database work, decide whether a newly resolved migration or schema failure should update `skills/project-database/references/memory.md`.

6. Final handoff should cover:
- what changed
- validations run
- residual risks
- next action if any

If a task brief exists, confirm whether the implementation is ready for that brief to move from `tasks/open/*` to `tasks/completed/*`.
Call out any missing or ambiguous verification rules that would block a deterministic QA follow-up.

7. Do not expand into a workflow engine or require structured handoff payloads between skills.
