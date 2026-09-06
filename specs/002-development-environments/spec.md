# Ender-3 V3 SE backup development environment

Provide locked repository tooling for this Cartesian printer backup and source-free
Docker, rootless Podman, and Apple container adapters. Preserve printer, Moonraker,
macro, calibration, snapshot, and retained archive contents exactly.

The gate checks documentation, shell/metadata syntax, and adapter behavior. It
does not provide a firmware parser or prove hardware safety. Review the active
include chain and model-specific configuration when those files change. No test
may connect, restore, flash, restart, heat, home, or move the printer. Local engine
runs preserve caller ownership and failure status. Apple execution requires a
supported Mac and Linux Nix builder and remains unverified on this host.
