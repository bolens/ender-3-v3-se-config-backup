# Ender-3 V3 SE configuration backup

[Documentation](docs/README.md)

Configuration and recovery history for this Cartesian printer. Review the active
`printer.cfg` include chain and the producing firmware before using a backup.
See [the delivery playbook](RELEASING.md) for review and recovery boundaries.

## Development tooling

See [development environments](docs/development-environments.md) for locked repository checks and local container adapters. Hardware verification remains separate.

## License scope and attribution

See [third-party notices](THIRD_PARTY_NOTICES.md) for the project license scope,
retained upstream notices, and dependency or asset exceptions.

## Recovery source distinctions

`factory_printer.cfg` identifies an Ender-3 Pro and a different board, not a
verified Ender-3 V3 SE factory restore. GuppyScreen includes imported CoreXY
belt and K1 material macros. Their presence does not establish compatibility
with this Cartesian printer. See the [legacy contract audit](specs/001-recovery-source-baseline/legacy-contracts.md)
for source ownership and unresolved firmware dependencies.
