# Task Briefs

Use `tasks/` for durable, versioned implementation briefs that feed the project skill workflow.

## Layout

- `tasks/open/`: active task briefs that still require implementation or validation
- `tasks/completed/`: completed task briefs moved out of the active queue after implementation and validation
- `tasks/templates/`: reusable task brief templates

## When To Use This Directory

Use a task brief when a feature needs a detailed, implementation-ready summary that combines:

- current codebase or UI findings
- requirement docs when relevant
- dependencies and build order
- acceptance criteria
- persistence considerations and open questions

## Workflow

1. Create a new task brief under `tasks/open/`.
2. Use the task brief as the durable input to `project-architect` and, when relevant, `project-database`.
3. Keep the brief updated as decisions are locked.
4. Do not begin development while the brief still contains unresolved items in `## Open Questions`. Resolve them first, or rewrite them into explicit decisions or deferred follow-ups that are out of scope for the current slice.
5. Use `bash scripts/tasks/validate-open-task-briefs.sh <task-brief-path>` to mechanically confirm the brief is ready before implementation starts.
6. After implementation, review, and QA confirm the feature works, sync any related backlog trackers such as `feature_tasks.md`.
7. Move the file to `tasks/completed/` only after implementation and validation are complete.

## Notes

- Task briefs are committed repo artifacts.
- Task briefs are distinct from `handoffs/<task-id>/scratchpad.md`, which remains untracked and temporary.
- Use stable IDs in filenames, for example `T-0001-sample-task.md`.

