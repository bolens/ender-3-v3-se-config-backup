# Agent guidance

[Documentation](docs/README.md) maps architecture, deployment, state, and document ownership.

Before changing printer configuration or macros, read [.specify/memory/constitution.md](.specify/memory/constitution.md)
and inspect the complete referenced Klipper or Moonraker include chain. For
prose-only edits, read the affected documentation and tracked configuration needed
to verify its claims. Use [RELEASING.md](RELEASING.md) for backup delivery and validation.

- Treat pin assignments, motion limits, homing, probing, heaters, and sensors as hardware-safety boundaries.
- Do not connect to, restart, flash, home, heat, or move the live printer without explicit authorization and a rollback plan.
- Preserve known-good snapshots and unrelated machine state. Never commit credentials, logs, databases, or transient runtime files.
- Validate syntax, duplicate sections, includes, and referenced macros statically; report what still requires hardware verification.

- Run `bash scripts/install-git-hooks` once per clone; hooks validate staged whitespace and Spec Kit metadata locally.

## Planning and evidence

Use the [project guide](.specify/memory/project-guide.md) and
[constitution](.specify/memory/constitution.md) for substantial changes. The guide
owns Spec Kit scope, retained history, retrospective requirements, and acceptance
evidence. Prose maintenance uses the normal repository workflow.

## Context and handoffs

- Search before reading. Use bounded source excerpts for exploratory reads over
  350 lines, and inspect required guidance and actual source before editing.
- When delegation is permitted, assign a bounded question or output, paths, and
  check. Return source locations, changes, and verification gaps for final review.
- Keep durable corrections in the [project guide](.specify/memory/project-guide.md)
  or owning contract. Replace superseded advice and read it before reuse.
  Temporary progress belongs in task notes. Preserve existing authority rules.
