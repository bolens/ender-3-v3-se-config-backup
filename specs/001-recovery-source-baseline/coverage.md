# Requirement coverage

| Requirement | Source and acceptance evidence |
| --- | --- |
| FR-001 | `printer.cfg` printer section and include chain; static include inventory, not calibration approval. |
| FR-002 | Tracked file inventory and immutable inspected revision; retained snapshots and archives are unchanged. |
| FR-003 | Static include inventory records unavailable/symlinked GuppyScreen and Helper-Script targets without dereferencing external paths. |
| FR-004 | RELEASING.md recovery sequence and project-guide operational limits; no automatic restore or printer operation. |

## Verification receipt

Static inspection parsed 6 available files in the active include chain using Python RawConfigParser with interpolation disabled and identified the Cartesian kinematics. External helper targets were listed without following symlinks. This is structural INI evidence, not validation by the producing vendor Klipper firmware. Native integration status, JSON/Bash syntax, whitespace, actionlint, and offline zizmor checks passed. Separate self-review confirmed recovery-source ownership and explicit external/firmware limitations. No archive/database contents were unpacked and no hardware operation was performed.

## Detailed audit receipt: 2026-09-06

[Detailed contracts](legacy-contracts.md) map 14 source families and all 44
available active macro definitions. [Source inventory](source-inventory.json)
records 18 structurally parsed configurations and three external include targets.
FR-005/FR-006/FR-008 map to eight file-boundary tests. FR-007 maps to five
numerical CLI subcases in one test. FR-009 maps to README recovery distinctions
and the factory/active source inspection.

All 14 native tests pass with no skips. Markdown, Ruff, Python compilation,
metadata hooks, actionlint, offline Zizmor and Nix syntax parsing pass. The
sensitive-file scan covered 104 files with no secrets or skipped files. Its 24
privacy indicators are pre-existing address examples/configuration values,
upstream author emails and an inactive commented home path. Separate self-review
confirmed the paired caller pins, unchanged printer configuration, source
inventory coverage and exact reuse of the tested offline helpers. No independent
reviewer ran. Hosted checks, final history scans and delivery remain pending.
