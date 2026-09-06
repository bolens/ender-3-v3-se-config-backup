# Agent guidance

Before Spec Kit planning or implementation, read
`.specify/memory/project-guide.md` with the project constitution. It maps
requirements to this repository's source, acceptance evidence, and validation.

Before changing printer configuration or macros, read `.specify/memory/constitution.md`
and inspect the complete referenced Klipper or Moonraker include chain. For
prose-only edits, read the affected documentation and tracked configuration needed
to verify its claims. Use `RELEASING.md` for backup delivery and validation.

- Treat pin assignments, motion limits, homing, probing, heaters, and sensors as hardware-safety boundaries.
- Do not connect to, restart, flash, home, heat, or move the live printer without explicit authorization and a rollback plan.
- Preserve known-good snapshots and unrelated machine state. Never commit credentials, logs, databases, or transient runtime files.
- Validate syntax, duplicate sections, includes, and referenced macros statically; report what still requires hardware verification.

- Run `bash scripts/install-git-hooks` once per clone; hooks validate staged whitespace and Spec Kit metadata locally.

## Spec-driven changes

Use Spec Kit for new capabilities, architecture, security-sensitive behavior,
migrations, and coordinated multi-file changes. Keep narrow fixes, dependency
updates, prose edits, and release housekeeping in the normal repository
workflow unless their risk warrants a written specification. Keep completed
feature directories under `specs/` as decision history. Backfill finished work
only when explicitly requested. Label those
specifications as retrospective baselines, record the inspected revision, and map
requirements to source and acceptance evidence. Separate observed behavior from
corrective requirements. Never imply the specification preceded its code or mark
unverified checks complete.

## Context and handoffs

- Locate source with targeted searches before reading. For exploratory reads of
  files over 350 lines, select relevant ranges. Read required guidance and actual
  source before edits or correctness claims; summaries do not replace them.
- When delegation is permitted, give each worker one question or concrete output,
  allowed paths, and a check. Return findings with source locations, changed paths,
  and verification gaps. Keep final review with the coordinating agent.
- Record durable user corrections in the [project guide](.specify/memory/project-guide.md)
  or owning contract with scope, reason, and evidence. Replace superseded advice;
  read relevant corrections before reusing assumptions. Keep temporary progress
  in task notes and preserve existing authority rules.
