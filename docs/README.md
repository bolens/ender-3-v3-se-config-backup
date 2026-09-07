# Documentation

Ender-3 V3 SE configuration and recovery ownership.

## Start here

| Need | Owning document |
| --- | --- |
| Use the project | [README.md](../README.md) |
| Change the repository | [AGENTS.md](../AGENTS.md) |
| Deliver or recover | [RELEASING.md](../RELEASING.md) |
| Plan substantial changes | [.specify/memory/project-guide.md](../.specify/memory/project-guide.md) |
| Non-negotiable constraints | [.specify/memory/constitution.md](../.specify/memory/constitution.md) |

## Architecture

[printer.cfg](../printer.cfg) and its includes define the active Cartesian printer configuration.
The [factory-named snapshot](../factory_printer.cfg) identifies a different printer and board.
It is not a verified Ender-3 V3 SE restore. The [recovery source audit](../specs/001-recovery-source-baseline/legacy-contracts.md)
records this mismatch and imported CoreXY/K1 material. Trace the active include chain before
selecting a macro or calibration file. K1 CoreXY settings are not interchangeable with this machine.

## Deployment and recovery

[RELEASING.md](../RELEASING.md) owns backup delivery and rollback planning. A repository check
cannot prove motion or heater safety. Applying a configuration requires a known-good snapshot and an
operator-controlled hardware verification sequence.

## Database and state

[Moonraker configuration](../moonraker.conf) is tracked configuration, not its running database.
Retained backup archives are recovery evidence and may contain private state. Do not unpack database
backups for routine documentation work or treat them as test fixtures.

## Documentation maintenance

Keep decisions, invariants, failure modes, and recovery requirements in the owning document. Link to
commands, defaults, schemas, and generated catalogs instead of copying them. Change the owner and
affected references together. Update this index when adding or moving a guide, and verify relative
links and heading anchors. Historical specs and audits describe their recorded revision, not current
runtime proof. A topic without an implementation stays explicitly unimplemented.

## Topic guides

- [Development environments](development-environments.md)

- [Editor setup](../.vscode/README.md)
- [License scope and attribution](../THIRD_PARTY_NOTICES.md)
- [Development container](../.devcontainer/README.md)
