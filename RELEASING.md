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
history, and an up-to-date branch with passing required checks, including
`Development environment` and `ci/woodpecker/pr/woodpecker`. These rules also apply
to administrators;
force pushes and branch deletion are disabled. Zero approving reviews are
required because this is a solo-maintainer repository; review the complete diff
before merging.

Keep required checks available on every pull request. Filter expensive work
inside jobs or use an always-running result job that rejects failures and
cancellations. Update the protection settings when renaming required jobs.

## Source lint

Woodpecker's `development-environment` step checks maintained Markdown with the
patterns in [`scripts/check-development.sh`](scripts/check-development.sh).
Keep coverage for the scope recorded in [`.github/source-lint.json`](.github/source-lint.json)
when adding documentation. The duplicate hosted
[Source lint workflow](.github/workflows/source-lint.yml) and its required context
are retired. Keep `ci/woodpecker/pr/woodpecker` and every retained current-head
check required; the [CI index](docs/woodpecker-transition.md) maps local commands
and native ownership.

Use the CI index's local entrypoints in the locked development environment.
Review the maintained-file scope when adding documentation; generated and
imported files retain their native validation. Retained platform, artifact,
deployment and release checks keep their existing authority.

## Woodpecker validation

[The transition contract](docs/woodpecker-transition.md) runs the existing locked
Linux development check on Woodpecker. Require actual native PR and merged-main
success before retiring duplicate hosted work. Preserve platform-specific, real
Docker, and administrative checks until equivalent replacement is verified.
This automation change does not deploy printer changes or create a release.
