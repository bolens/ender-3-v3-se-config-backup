# Plan: Cartesian printer recovery source

The [specification](spec.md) preserves existing behavior. Use the project guide
and constitution for implementation constraints. Keep upstream-managed templates,
helpers, and integration manifests unchanged.

## Source ownership

- `printer.cfg`
- `printer_params.cfg`
- `gcode_macro.cfg`
- `sensorless.cfg`
- `moonraker.conf`

## Constitution check

Keep the repository constitution, authoritative source files, existing interfaces, and native validation. The baseline does not authorize live host mutation, publication of private data, or changes to managed Spec Kit files.

## Validation

```sh
bash .githooks/pre-push
git diff --check
actionlint
zizmor --offline --min-severity medium --min-confidence medium .github
```

Run checks in an isolated checkout. Commands are instructions, not evidence of
a pass. Record results in `coverage.md`, keep incomplete work in `tasks.md`, and
follow `RELEASING.md` for reviewed delivery. No live operation is required solely
to create this retrospective baseline.
