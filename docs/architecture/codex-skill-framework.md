# Codex Skill Framework

## Purpose

This framework uses repo-owned Codex skills to keep implementation aligned with project conventions without introducing a workflow engine.

Skills live under `skills/`, standards live under `docs/architecture/standards/`, and the main Codex agent remains the only orchestrator.

For a non-technical overview of how the agent, skills, and task briefs work together, see [docs/agent-skill-task-guide.md](../agent-skill-task-guide.md).

## Core Model

- User prompts stay in plain language.
- The main Codex agent selects the relevant skill or skills.
- Skills provide lightweight repo-specific guidance and never invoke each other.
- Standards docs are the canonical source of implementation rules.
- Scratchpads are optional, task-scoped, and untracked.
- Reasoning certificates are selective and only required for analysis-heavy or high-risk claims.
- Per-skill memory notes are limited to recurring, reusable domain lessons after verified fixes or settled conventions.

## Repo-Local Skill Availability

- The skills under `skills/` are repo-local guidance for work performed inside this repository.
- They are available even when a generic installed-skill inventory shown at thread start does not list them.
- When work begins in this repository, the main agent should inspect `skills/` directly instead of assuming the generic skill inventory is complete.

## Skills

- `project-architect`: cross-domain analysis, file targeting, interface mapping, and validation selection
- `project-backend`: service, API, auth, repository, model, and backend test work
- `project-frontend`: routes, layouts, screens, components, hooks, and HTTP boundary work
- `project-database`: migrations, schema alignment, and DB verification work
- `project-docs`: canonical docs, manifests, standards, and traceability updates
- `project-qa`: browser-based smoke verification and reusable QA wrappers
- `project-review`: final validation, regression review, standards compliance, and residual-risk checks

## Standards Loading Rules

Skills should read the relevant standards doc before coding:

- frontend: `docs/architecture/standards/frontend-ui.md`
- backend: `docs/architecture/standards/backend.md`
- database: `docs/architecture/standards/database.md`

Standards docs are canonical. Skills should summarize or point to them, not duplicate them.

## Main-Agent Selection Rules

- The main Codex agent is the only orchestrator.
- At the start of every new thread in this repository, select and read at least one relevant `skills/project-*/SKILL.md` file before substantial work begins.
- Start with `project-architect` when a task is ambiguous, cross-domain, or risky.
- Start directly with a domain skill for obvious single-domain work.
- Use `project-review` before final handoff on substantial tasks.
- Use `project-docs` only when docs or manifests actually need changes.
- A skill never invokes another skill. The main agent decides the next skill.

## Skill Announcements

- Before substantial work begins, announce the skill or skills being used.
- When switching domains or changing the active skill, announce the new skill being used.
- Keep the announcement to one short line.
- The announcement is informational only and does not create a workflow gate or payload contract.

## Baton And Scratchpad

Keep the normal baton in conversation.

Use an optional scratchpad only for substantial, cross-domain, or multi-session work:

- path: `handoffs/<task-id>/scratchpad.md`
- git policy: untracked
- owner: main Codex agent
- purpose: carry current task state, not standards or durable knowledge

Suggested scratchpad shape:

```md
# Task Scratchpad

## Objective
<one-line goal>

## Decisions Locked
- ...

## Relevant Files
- ...

## Validation Status
- Pending:
- Passed:

## Open Questions
- ...

## Next Step
- ...
```

## Task Briefs

Use committed task briefs for durable, implementation-ready requirements:

- path: `tasks/open/<task-id>.md`
- move to: `tasks/completed/<task-id>.md` after implementation and validation are complete
- purpose: combine current codebase findings, requirements consulted, dependencies, acceptance criteria, persistence questions, and verification rules in one durable brief
- template: `tasks/templates/task-brief-template.md`

Task briefs are committed repo artifacts. They are distinct from untracked `handoffs/<task-id>/scratchpad.md` files.

## Skill Memory

Skills may keep reusable domain memory in:

- `skills/<skill-name>/references/memory.md`

Rules:

- record only reusable lessons
- update only after diagnosis and a verified fix or a settled repo convention
- do not store task-specific state, raw run logs, or open questions there
- keep task-specific planning in `tasks/*`
- keep temporary state in `handoffs/*`

## Reasoning Certificates

Use reasoning certificates selectively:

- required for `project-architect` on analysis-heavy or high-risk work
- required for `project-review` when making static analysis claims without execution
- optional elsewhere when tests or runtime checks are not available

## Support Commands

- validate all skills:

```bash
bash scripts/codex/validate-skills.sh
```

- validate that open task briefs have no unresolved open questions:

```bash
bash scripts/tasks/validate-open-task-briefs.sh
```
