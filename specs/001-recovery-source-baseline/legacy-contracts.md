# Detailed recovery-source contracts

Inspected revision: `2b234ab0f3ef11c3ea1489d4ba133d6d4cbe7afa`, 2026-09-06.
This retrospective audit records source ownership and observed behavior. It does
not certify a hardware restore. The active printer uses Cartesian kinematics.

| Contract | Source | Observed behavior and limits |
| --- | --- | --- |
| ER-001 | `printer.cfg`, `printer_params.cfg`, parameter macros | Own board pins, Cartesian axis limits, currents, BLTouch/vendor pressure probing, extrusion, heaters, fans, resonance sensor and saved mesh/shapers. Parameter macros retain separate dimensions and operating defaults. These values remain machine-specific. |
| ER-002 | `sensorless.cfg` | Homing override tracks readiness/movement flags, performs forced Z clearance and repeated XY homing, centers using BLTouch offsets and restores a default mesh. Vendor mesh commands and physical endstop behavior require producing firmware. |
| ER-003 | `gcode_macro.cfg` lifecycle | Pause/resume tracks lift and hotend target, checks homing/extrusion state and parks. Cancellation shuts down heaters/fans/motors and resets motion/extrusion defaults. FIRST_FLOOR paths have distinct parking and extrusion behavior. |
| ER-004 | `gcode_macro.cfg` adapters | M900 maps pressure advance, M204 forwards acceleration arguments, M205 sets corner velocity, M106 scales the primary fan and M107 stops it. Missing-parameter and firmware compatibility findings remain below. |
| ER-005 | `gcode_macro.cfg` material | Load/unload wait for configured extrusion temperature and preserve G-code state. M600 pauses then performs relative extrusion/retraction and restores E position. These are physical operations, never validation fixtures. |
| ER-006 | `gcode_macro.cfg` calibration | Mesh, shaping and Z-offset macros invoke vendor calibration/save commands. AUTOTUNE_SHAPERS has an empty body and supplies no tuning implementation. INPUTSHAPER_X/Y differ from the parameterized INPUTSHAPER path. |
| ER-007 | `GuppyScreen/guppy_cmd.cfg` | Connects physical resonance acquisition with plotting commands and shell-service hooks. CoreXY half-axis belt acquisition and K1 fan helpers are imported compatibility findings, not validated Cartesian features. Sustained excitation validates axis labels but still requires hardware context. |
| ER-008 | `Helper-Script/camera-settings.cfg` | Reads or adjusts six camera-control interfaces through v4l2-ctl on a fixed video device. Descriptions state ranges but macros do not enforce them. Driver availability and quoted-parameter parsing remain external runtime dependencies. |
| ER-009 | `moonraker.conf`, `mobileraker.conf` | Retain server/socket/upload/history behavior, trusted-client and CORS policy, update sources, camera and companion settings. Parsing does not prove authentication, network reachability or service operation. |
| ER-010 | External helper symlinks and `Helper-Script/variables.cfg` | Guppy updater, Git backup and Z-offset helpers are external dependencies. The variables file retains one Z-offset value as recovery state, not a current measurement. Targets were not dereferenced. |
| ER-011 | `GuppyScreen/scripts/calibrate_shaper.py`, `shaper_calibrate.py`, `shaper_defs.py` | Parse raw/PSD logs, combine frequency bins, normalize and estimate shaper vibration/smoothing, then produce image/CSV and JSON outputs. All four original plotting helpers exactly match the separately audited K1 source revision. Numerical estimates do not establish hardware suitability. |
| ER-012 | `GuppyScreen/scripts/graph_belts.py`, `plot_output.py` | Compare two raw captures with peak pairing, similarity and optional spectrogram. Explicit offline mode avoids Linux process inspection for completed captures; default waiting remains. Image replacements are staged in the destination filesystem. CSV writes keep their existing behavior. |
| ER-013 | Factory, board-specific and dated snapshots; retained archives | `factory_printer.cfg` identifies an Ender-3 Pro with different board assumptions. Six dated snapshots and a board-named reference remain historical evidence. Backup archives are retained without unpacking, and database contents are not inspected. None is automatically selected for restore. |
| ER-014 | Development adapter, editor tasks, hooks and CI | The development-environment specification owns source-free image construction and local engine argument/status behavior. Native gates cover metadata, maintained source and offline numerical fixtures. They do not operate the printer. |

## Active macro inventory

The six available active files define 44 macros. External definitions are outside
this count. Empty parameter/state macro bodies store variables, not actions.

| Contract | Macro definitions |
| --- | --- |
| ER-001 | `PRINTER_PARAM`, `STRUCTURE_PARAM` |
| ER-002 | `xyz_ready`, `_IF_HOME_Z`, `_IF_MOVE_X`, `_IF_MOVE_Y`, `_HOME_X`, `_HOME_Y`, `_HOME_Z` |
| ER-003 | `CANCEL_PRINT`, `PAUSE`, `RESUME`, `FIRST_FLOOR_PAUSE`, `FIRST_FLOOR_PAUSE_POSITION`, `FIRST_FLOOR_RESUME`, `FINISH_INIT` |
| ER-004 | `M900`, `M204`, `M205`, `M106`, `M107` |
| ER-005 | `LOAD_MATERIAL`, `QUIT_MATERIAL`, `M600` |
| ER-006 | `G29`, `PRINT_CALIBRATION`, `INPUTSHAPER`, `INPUTSHAPER_X`, `INPUTSHAPER_Y`, `AUTOTUNE_SHAPERS`, `Z_OFFSET_TEST`, `Z_COMPENSATE_TEST`, `ZZ_OFFSET_TEST` |
| ER-007 | `GUPPY_SHAPERS`, `GUPPY_BELTS_SHAPER_CALIBRATION`, `GUPPY_EXCITATE_AXIS_AT_FREQ`, `_GUPPY_LOAD_MATERIAL`, `_GUPPY_QUIT_MATERIAL` |
| ER-008 | `CAM_SETTINGS`, `CAM_BRIGHTNESS`, `CAM_CONTRAST`, `CAM_SATURATION`, `CAM_HUE`, `CAM_WHITE_BALANCE_TEMPERATURE_AUTO` |

## Unresolved configuration findings

- `factory_printer.cfg` describes Ender-3 Pro hardware. Preserve it as a distinct reference.
- The active Guppy belt macro explicitly targets CoreXY half axes. Its acquisition model is not validated for the Cartesian Ender.
- `_GUPPY_LOAD_MATERIAL` references K1 fan helpers absent from available active files. Missing external includes prevent complete resolution.
- M106 uses `tmp` outside the branch that defines it when S is supplied. Its no-S behavior needs a compatible template/firmware check before changing fan control.
- `_HOME_X` has `G91 X5 F2000` where the Y path separates mode selection and movement. Intended physical motion needs firmware/operator confirmation.
- FINISH_INIT resets acceleration/deceleration to 5000 despite lower active configuration values. Do not infer that the reset is a validated safe operating limit.
- Parameter macros contain a 240 mm Z maximum while the active stepper permits 250 mm. Preserve the distinction pending machine context.

No printer configuration or macros changed in this pass. Producing firmware,
external helpers and physical verification remain unavailable. The public
recovery description now exposes these distinctions.

## Offline acceptance

The static inventory parsed 18 regular configuration/reference files with
RawConfigParser and interpolation disabled, found six available active files,
three external include symlinks and 44 macros, and reported no within-file
structural parse errors. Cross-file overrides and vendor grammar are separate
from this structural check. Archive/database contents and symlink targets were
not read. [Source inventory](source-inventory.json) records the section/include map.

Corrective FR-005 through FR-008 use the same file-boundary and synthetic numerical
fixtures as K1 Max, against byte-identical original helpers. All 14 native tests pass for this repository, with no skips. Hosted checks
and delivery remain pending.
