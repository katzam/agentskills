# Project Repository Notes

## Scope
This repository uses repo-managed Codex skills under `skills/`, but the main Codex agent remains the only orchestrator. Skills are lightweight repo guidance, not workflow stages or agent handoff payloads.

## Repo-Local Skill Bootstrap
- Treat the repo-local skills under `skills/` as mandatory guidance for this repository.
- These repo-local skills are available even when they are not listed in a generic installed-skill inventory shown at thread start.
- At the start of every new thread opened in this repository, select and read at least one relevant `skills/project-*/SKILL.md` file before substantial work begins.
- If the task is ambiguous, cross-domain, or high-risk, start with `skills/project-architect/SKILL.md`.
- If the task is clearly single-domain, start with the matching domain skill directly.
- Use `skills/project-review/SKILL.md` before final handoff on substantial tasks.
- Do not ignore repo-local skills just because the user did not name them explicitly.

## Startup Checklist
1. Read [docs/README.md](docs/README.md) for canonical framework sources.
2. Read [docs/architecture/repo-map.md](docs/architecture/repo-map.md) for code ownership and file locations.
3. If the task affects the framework or domain conventions, read [docs/architecture/codex-skill-framework.md](docs/architecture/codex-skill-framework.md) and the relevant file under `docs/architecture/standards/`.
4. Confirm the impacted domains before editing: `frontend`, `backend`, `database`, `docs`, `scripts`, `skills`, `tasks`.
5. Keep work scoped to one coherent objective.

## Workflow
1. Discover: inspect the relevant code and docs before editing.
2. Plan: identify the exact files to change, the skills or standards involved, and the checks that must pass.
3. Readiness gate: if the active task brief under `tasks/open/*` still has unresolved items in `## Open Questions`, do not begin implementation. Resolve the questions first, or rewrite them into explicit decisions or deferred follow-ups in the brief. Use `bash scripts/tasks/validate-open-task-briefs.sh <task-brief-path>` as the mechanical readiness check.
4. Implement: keep changes minimal and aligned with existing repo patterns.
5. Validate: run the domain checks that match the modified surfaces.
6. Review: confirm the final state still satisfies the original task and does not leave dead references.

## Skill Announcements
- Before substantial work begins, state the repo skill or skills being used.
- When switching domains or changing the active skill, state the new skill being used.
- Keep the announcement to one short line and make it informational only.

## Skill Selection Gate
- `project-architect` is for discovery, impact analysis, validation planning, and task briefs.
- Do not start implementation edits under `project-architect` alone unless the task changes only `docs/*`, `tasks/*`, or repo operating notes such as `AGENTS.md`.
- Before the first edit in a frontend surface, load and announce `skills/project-frontend/SKILL.md`.
- Before the first edit in a backend surface, load and announce `skills/project-backend/SKILL.md`.
- Before the first edit in database or migration surfaces, load and announce `skills/project-database/SKILL.md`.
- Before the first edit in canonical docs, manifests, standards, or repo operating notes, load and announce `skills/project-docs/SKILL.md`.
- For cross-domain implementation, `project-architect` may be used first, but the agent must switch to the concrete domain skill or skills before the first edit in each domain.
- If the touched file set expands into a new domain mid-task, stop, load the matching skill, announce the switch, and only then continue editing.
- If the matching domain skill has not been loaded, do not edit that domain.
- Use `skills/project-review/SKILL.md` before final handoff on substantial implementation tasks.

## Quality Gates
| Domain | Required commands |
| --- | --- |
| Frontend changes | Replace with the repo's frontend lint and build commands |
| Backend changes | Replace with the repo's backend test command |
| Runtime DB apply/verify | Replace with the repo's schema apply and verify command |
| Codex skill changes | `bash scripts/codex/validate-skills.sh` |
| Bash script changes | `bash -n <script-path>` |

## Definition Of Done
- Requested behavior is implemented and validated with the relevant commands.
- Task briefs and any related backlog trackers reflect the final state.
- Schema work is source-controlled through migration assets plus verification evidence, not ad hoc DB mutation.
- Canonical standards remain in `docs/architecture/standards/*`; skills should reference them rather than duplicate them.
- Final handoff includes what changed, validation run, residual risks, and next action if any.

## Guardrails
- Keep repo-managed skills under `skills/`; do not create orchestrator, router, or run-graph skills.
- Keep repo skills repo-local only; do not install them into `~/.codex/skills`.
- Do not rely on the generic installed-skill list to discover repo skills; inspect `skills/` directly when starting work in this repository.
- Keep the normal skill baton in conversation. Use `handoffs/<task-id>/scratchpad.md` only for substantial, cross-domain, or multi-session work, and keep scratchpads untracked.
- Use per-skill `references/memory.md` files only for recurring, reusable domain lessons after a verified fix or settled convention. Do not use them as scratchpads, task logs, or a replacement for `tasks/*`.
- Keep durable, versioned implementation briefs under `tasks/open/*`; move them to `tasks/completed/*` only after implementation and validation are complete.
- Treat unresolved `## Open Questions` in a task brief as an implementation blocker, not as optional notes.
- Use reasoning certificates selectively for analysis-heavy or high-risk claims, not for routine coding.
- Replace the placeholder validation commands in this file before relying on the framework for production work.
