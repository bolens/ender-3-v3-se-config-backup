# Requirement coverage

| Requirement | Source and acceptance evidence |
| --- | --- |
| FR-001 | `printer.cfg` printer section and include chain; static include inventory, not calibration approval. |
| FR-002 | Tracked file inventory and immutable inspected revision; retained snapshots and archives are unchanged. |
| FR-003 | Static include inventory records unavailable/symlinked GuppyScreen and Helper-Script targets without dereferencing external paths. |
| FR-004 | RELEASING.md recovery sequence and project-guide operational limits; no automatic restore or printer operation. |

## Verification receipt

Static inspection parsed 6 available files in the active include chain using Python RawConfigParser with interpolation disabled and identified the Cartesian kinematics. External helper targets were listed without following symlinks. This is structural INI evidence, not validation by the producing vendor Klipper firmware. Native integration status, JSON/Bash syntax, whitespace, actionlint, and offline zizmor checks passed. Separate self-review confirmed recovery-source ownership and explicit external/firmware limitations. No archive/database contents were unpacked and no hardware operation was performed.
