# Agent, Skills, And Task Guide

## Purpose

This document explains, in plain language, how this framework uses the Codex agent, repo skills, and task files to manage development work.

The short version is:

- there is one main agent
- the main agent uses skills as guidance
- task files describe the work in a durable way
- review and QA confirm whether the work is actually done

This framework is meant to stay simple enough to drop into another app repository.

## The Simple Model

### The Agent

The agent is the main working assistant for the project.

It is responsible for:

- reading the codebase and docs
- deciding which project skill applies
- making code changes
- running the right validation
- coordinating review and QA
- reporting what changed and what still needs attention

There is only one orchestrator.

We do not have a swarm of agents handing work to each other behind the scenes. The main agent stays responsible for the whole task from start to finish.

### Skills

Skills are not separate workers. They are repo-owned instruction sets.

A skill tells the main agent how to work well in a specific area of the project.

Examples:

- `project-frontend` helps with UI and client-side changes
- `project-backend` helps with service and API changes
- `project-database` helps with schema and migration changes
- `project-review` helps with final review and risk checking
- `project-qa` helps with browser testing and repeatable smoke flows

The agent chooses the right skill or skills based on the request.

Some skills may also keep a small `references/memory.md` file.

That file is for reusable lessons in that domain, such as a recurring migration trap, a frontend composition pitfall, or a QA environment gotcha.

It is not a task log and it does not replace task briefs.

### Task Files

Task files are the durable written instructions for a feature or change.

They live in:

- `tasks/open/` for active work
- `tasks/completed/` for finished work

These task files are important because they turn a rough request into something concrete and testable.

A good task file explains:

- what we are trying to achieve
- what is in scope and out of scope
- what parts of the app are affected
- what the required behavior is
- how we will tell if the feature works

### Requirement Documents

If your project stores canonical requirement docs as `.docx` files under `docs/`, this framework supports searchable Markdown mirrors under:

- `docs/requirements/source/markdown/`

The map between canonical requirement sources and generated mirrors is tracked in:

- `docs/requirements/source-manifest.md`

If your project does not use `.docx` files, you can keep this part minimal or remove it.

## The Different Kinds Of Project Records

### `feature_tasks.md`

This is the high-level backlog.

It helps answer:

- what major features are still incomplete
- what broad area should we work on next

It is not usually detailed enough to implement directly.

### `tasks/open/*.md`

These are implementation-ready task briefs.

They are more specific than the backlog and are the normal starting point for real work.

### `tasks/completed/*.md`

These are finished task briefs that have already been implemented and validated.

They create a history of what was done and how it was verified.

## How Work Normally Flows

### 1. Start With A Backlog Item Or Plain Request

Work usually begins in one of two ways:

- you point to an item in `feature_tasks.md`
- you describe a feature or problem in plain English

### 2. Create Or Refine The Task Brief

The task brief is where the request becomes precise.

This step usually includes:

- checking the current code
- checking requirement docs if needed
- deciding which frontend, backend, or database surfaces are affected
- writing clear verification rules

The verification rules matter because they answer:

"What would have to be true for us to say this feature works?"

### 3. What Happens Inside An Implement Request

When you ask the agent to implement a task, the main agent handles the full internal workflow on its own.

That means the user does not need to manually tell it when to switch from coding to review or when to start QA.

Inside one normal implementation request, the main agent will usually:

- use the right project skill guidance
- make the code and configuration changes
- run the matching validation
- perform the internal review step
- perform the QA step when the feature requires it and the environment is available
- decide what to fix next if a problem is found

Depending on the task, that may involve:

- frontend work
- backend work
- database work
- documentation updates
- QA wrapper updates

### 4. Mark The Work Complete

Once implementation, review, and QA are all in good shape:

- the task brief moves from `tasks/open/` to `tasks/completed/`
- related backlog items are updated if needed
- the final handoff explains what changed and how it was validated

## What "Done" Means

A feature is not considered done just because code was written.

It is only done when:

- the requested behavior is implemented
- the right validation has been run
- review does not find blocking issues
- QA confirms the feature works
- the task and backlog records are updated
