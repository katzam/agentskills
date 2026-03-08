# Database Memory

Use this file only for recurring, reusable migration, schema, or persistence lessons after a real failure or meaningful warning has been diagnosed, fixed, and verified.

## Rules Of Thumb

- Record only reusable lessons that are likely to prevent repeated mistakes.
- Do not add one-off typos, unresolved failures, or raw command output.
- Use DB apply output, report files, and the verified fix as the evidence for any new entry.

## Known Failure Patterns

No recurring failure patterns have been captured yet.

Add entries in this format:

### <short title>
- Symptom: <error or verify failure summary>
- Cause: <actual root cause>
- Fix: <what resolved it>
- Guardrail: <how to avoid it next time>
- Example paths: <relevant files if helpful>

## Verification Reminders

- Run the repo's schema apply or migration verification commands after migration changes.
- Confirm both migration state and schema verification checks pass before closing the task.
- If the fix changed persistence behavior, run backend tests as well.

