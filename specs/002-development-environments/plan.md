# Implementation plan

Use pinned devenv/nixpkgs for Bash, GNU utilities, jq, Python, Markdown lint, Ruff,
ShellCheck, and workflow validation. Wrap the existing metadata pre-push gate and
add adapter regressions. Keep Ender-3 V3 SE Cartesian configuration and recovery files
outside the write scope; repository tooling does not replace firmware-specific
syntax review or operator-controlled hardware verification.

Add filtered Linux/macOS CI, actual Docker validation, cancellation, and an always
reporting gate. Validate native and rootless Podman paths before protected PR
delivery. Verify main and clean the completed branch. No release tag or hardware
application is needed for this tooling-only change.
