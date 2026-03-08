---
name: project-qa
description: Browser-based and runtime QA guidance for this project. Use when a task needs real browser verification, reusable smoke wrappers, or environment-aware end-to-end validation.
---

Use this skill when a task needs real runtime verification.

1. Read:
- `AGENTS.md`
- `docs/architecture/repo-map.md`
- `docs/architecture/standards/frontend-ui.md`
- `references/memory.md`

When a task brief under `tasks/open/*` or `tasks/completed/*` is provided, read it before running QA flows and treat it as the acceptance-criteria anchor.
When the brief includes verification rules, use them to decide which browser flows, direct API calls, and side-effect checks to run.

2. Prefer the repo-owned wrappers under `scripts/qa/*` over global browser tooling.
When a task needs a reusable verification flow that does not already exist, `project-qa` is the skill that should add or update the corresponding wrapper under `scripts/qa/*`.

3. Default QA workflow:
- run the relevant static checks first
- turn the task brief's verification rules into the smallest set of deterministic UI, API, and data checks
- deploy or refresh the runtime first if `AGENTS.md` or the task brief says live verification requires it
- add or extend a repo-owned wrapper under `scripts/qa/*` when the verification rules justify a repeatable smoke flow
- capture the artifact path and environment assumptions in the handoff

4. Keep QA runs deterministic:
- prefer labels, roles, and visible text over brittle selectors
- keep browser sessions isolated per run
- prefer direct backend calls when the verification rule is API- or data-oriented rather than purely visual
- save screenshots or other artifacts outside the repo unless a task explicitly needs committed fixtures

5. When the smoke flow cannot run because the app is down or a required local dependency is missing, report the blocker precisely instead of fabricating a pass.
