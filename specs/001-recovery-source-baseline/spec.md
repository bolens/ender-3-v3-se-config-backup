# Feature specification: Cartesian printer recovery source

**Created**: 2026-09-05
**Status**: Retrospective baseline
**Inspected revision**: `10efd275f3eff70f965c4aa315e9a9b40717eebc`
**Input**: The owner requested a fleet-wide Spec Kit retrofit and implementation audit.

Retained printer configuration and history identify a recovery source for this specific machine, separate from firmware validation and hardware readiness.

This specification records existing contracts after implementation. It does not
claim that the original work followed Spec Kit. New behavior requires a separate
change contract. Existing feature specifications remain authoritative within their
own scope.

## User scenarios and testing

### User story 1: Use documented source (P1)

A maintainer selects the supported source or entry point.

**Acceptance**: Behavior and outputs match the requirement mapping below.

### User story 2: Handle boundary cases (P2)

Inputs are invalid or optional content is missing.

**Acceptance**: Named source checks preserve explicit failure or fallback behavior.

### User story 3: Maintain the contract (P3)

A future change affects this baseline.

**Acceptance**: Revise the owning source, documentation, and acceptance evidence together.

## Requirements

- **FR-001**: The active printer configuration MUST retain its machine-specific Cartesian motion and include ownership.
- **FR-002**: Current configuration, factory references where present, dated snapshots, and archives MUST remain distinguishable recovery evidence.
- **FR-003**: External helper includes MUST be identified as dependencies rather than silently treated as available configuration.
- **FR-004**: Restore and hardware testing MUST remain explicitly scoped to compatible firmware/hardware, with current configuration preserved first.

## Success criteria

- **SC-001**: Every requirement has a named source owner and acceptance check in `coverage.md`.
- **SC-002**: The listed native checks pass for the reviewed candidate, with unavailable environments and operational checks recorded separately.
- **SC-003**: Retrofitting preserves existing interfaces and completed specifications. Any confirmed implementation gap is corrected under an explicit requirement before it is marked complete.

## Edge cases and operational limits

Vendor Klipper modules, external includes, physical wiring, calibration, homing, heating, and restore readiness are unverified. Static syntax does not establish printer safety. The producing firmware is not available for a full configuration load; preserve existing configuration values and obtain compatible firmware/hardware evidence before any restore.

## Detailed legacy audit: 2026-09-06

[Detailed contracts](legacy-contracts.md) distinguish active Cartesian configuration
from imported and retained references. Corrective plotting requirements follow.

- **FR-005**: Both plot log readers MUST accept raw accelerometer CSV with or without leading comments and reject empty input with a clear error.
- **FR-006**: Both plot commands MUST preserve an existing plot image if rendering its replacement fails and remove temporary output owned by the failed invocation.
- **FR-007**: Changing the plot frequency limit MUST preserve matching frequency/response array lengths. Displaying raw data above the model's calculation range MUST NOT extrapolate a shaper prediction outside that range.
- **FR-008**: Belt plotting MUST provide an explicit `--offline` mode for completed CSV captures that does not inspect live process descriptors. The default mode MUST retain waiting for capture files to close.

- **FR-009**: Recovery documentation MUST identify `factory_printer.cfg` as an Ender-3 Pro reference and imported CoreXY/K1 macros as compatibility findings, without implying they are validated Ender-3 V3 SE recovery defaults.
