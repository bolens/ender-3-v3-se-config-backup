# Printer Configuration Constitution

## Core Principles

### I. Hardware-Specific Source of Truth
Tracked Klipper, Moonraker, screen, and macro files MUST describe the documented printer hardware. Machine-specific calibration MUST remain explicit and MUST NOT be generalized to other printers.

### II. Motion and Thermal Safety
Changes to limits, homing, probing, heaters, motors, sensors, and macros MUST preserve safe bounds and fail safely. Live printer actions require explicit operator authorization.

### III. Preserve Recovery Evidence
Known-good snapshots and vendor configuration are recovery assets. Changes MUST remain reviewable and MUST NOT discard history without an explicit retention decision.

### IV. Separate Secrets and Runtime State
API keys, credentials, camera secrets, logs, databases, and transient runtime state MUST remain untracked. Public examples use placeholders.

### V. Verify Offline Before Hardware
Includes, sections, macros, pins, and referenced files MUST be checked statically first. Hardware verification requires a controlled plan and documented rollback.

## Governance

This repository governs one printer configuration. Safety-impacting exceptions require hardware context, validation evidence, and a constitution version update.

**Version**: 1.0.0 | **Ratified**: 2026-09-02 | **Last Amended**: 2026-09-02
