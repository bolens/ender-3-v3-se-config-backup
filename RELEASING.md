# Backup delivery playbook

[Documentation](docs/README.md)

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

## Branch protection

The default branch requires pull requests, resolved conversations, linear
history, and an up-to-date branch with passing required checks, including `lint
/ actionlint` and `lint / zizmor`. These rules also apply to administrators;
force pushes and branch deletion are disabled. Zero approving reviews are
required because this is a solo-maintainer repository; review the complete diff
before merging.

Keep required checks available on every pull request. Filter expensive work
inside jobs or use an always-running result job that rejects failures and
cancellations. Update the protection settings when renaming required jobs.

## Source lint

The Source lint workflow checks maintained markdown files selected by
[`.github/source-lint.json`](.github/source-lint.json) on every pull request
and push to `main`. Existing native checks remain part of the merge gate.
Use the [shared local reproduction instructions](https://github.com/bolens/.github/blob/7603518f305fb76f7bb1b9979f2692521f633b82/docs/source-lint.md)
with the same tooling revision pinned in
[the workflow](.github/workflows/source-lint.yml). Review exclusions when adding
source files; generated and imported files retain their native validation.
Require the new check to pass on the current PR head before merging.
