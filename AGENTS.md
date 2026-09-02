# Agent guidance

Read `.specify/memory/constitution.md` and inspect every referenced Klipper or Moonraker include before editing.

- Treat pin assignments, motion limits, homing, probing, heaters, and sensors as hardware-safety boundaries.
- Do not connect to, restart, flash, home, heat, or move the live printer without explicit authorization and a rollback plan.
- Preserve known-good snapshots and unrelated machine state. Never commit credentials, logs, databases, or transient runtime files.
- Validate syntax, duplicate sections, includes, and referenced macros statically; report what still requires hardware verification.

- Run `bash scripts/install-git-hooks` once per clone; hooks validate staged whitespace and Spec Kit metadata locally.
