# Backup delivery playbook

This repository is a continuously updated printer-configuration backup. It has
no versioned releases; immutable Git commits are recovery points.

## Prepare and validate

Capture only the intended Ender 3 V3 SE configuration. Exclude credentials,
network identifiers, transient logs, caches, generated jobs, and unrelated
printer state. Review the complete diff and validate configuration syntax with
the printer software version that produced it. Record any firmware or hardware
assumption in the commit or README.

## Review, deliver, and verify

Use a pull request and squash merge to protected `main`; do not push a backup
directly. Confirm CI passes and the merged tree can be parsed without access to
the live printer. Delivery does not authorize writing files back to a printer.

## Recover

Restore only from a reviewed commit compatible with the target firmware and
hardware. Preserve the printer's current files first. Apply and restart through
the printer's documented recovery path, then verify heaters, axes, endstops,
and safety limits before printing.

Fleet policy: <https://github.com/bolens/.github/blob/main/RELEASING.md>.
