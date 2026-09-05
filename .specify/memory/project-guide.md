# ender-3-v3-se-config-backup Spec Kit project guide

Configuration and recovery history for the Ender-3 V3 SE with Cartesian motion.

Read this guide with `AGENTS.md` and `.specify/memory/constitution.md` before
specifying, planning, or implementing a substantial change. It is project-owned
guidance, not an upstream-managed template.

## Source and ownership map

- `printer.cfg`
- `factory_printer.cfg`
- `printer_params.cfg`
- `gcode_macro.cfg`
- `sensorless.cfg`
- `moonraker.conf`

## Specification and plan decisions

Identify the active include chain and distinguish current configuration, factory
reference, dated snapshots, and archived backups. Tie pin, probe, motor, heater, and
motion decisions to this printer. Do not import K1/CoreXY assumptions.

## Acceptance evidence

Review include targets, duplicate sections, macro references, units, safe limits,
homing/probing order, and failure behavior. Specify a known-good rollback and an
operator-controlled hardware test sequence without executing it during repository
validation.

## Validation and operational limits

```sh
git diff --check
```

The repository does not ship an automated proof of printer safety. Record static
inspection separately from unperformed hardware checks. Do not unpack retained database
backups, expose their contents, connect, flash, restart, heat, home, or move the
printer.

## Working through Spec Kit

Use Spec Kit for new capabilities, architectural or security-sensitive changes,
migrations, and coordinated changes that need a written contract. Keep narrow fixes,
dependency updates, and prose maintenance in the normal PR workflow.

For a new feature, record observable acceptance criteria in `spec.md`, source ownership
and constitution checks in `plan.md`, and evidence-bearing work in `tasks.md` under the
feature directory created by Spec Kit. Resolve material unknowns before implementation.
Mark tasks complete only after their stated verification, and distinguish completed,
skipped, blocked, and manual checks. Retain completed feature documents as decision
history; do not backfill feature specifications for already finished code.

Keep `.specify/templates/`, `.specify/scripts/`, and generated Codex skills under their
integration manifests. Use this guide and the constitution for local customization.
Regenerate managed files through Spec Kit and verify that project-owned memory survives
updates. Follow `RELEASING.md` for push, merge, release or delivery, and recovery.
