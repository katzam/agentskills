Use the repo-local skill named by `$ARGUMENTS`.

Steps:
1. Check whether `skills/$ARGUMENTS/SKILL.md` exists.
2. If it exists, read it before substantial work and follow its instructions for the current task.
3. Announce the active skill in one short line.
4. If it does not exist, say so briefly and continue with the best fallback.

Keep `skills/` as the canonical skill source. Do not create a duplicate skill body under `.claude/commands/`.

