# M14 One UI 9 Port — early development

Experimental development workspace targeting Samsung Galaxy M14 5G (SM-M146B / `m14x`) and an Android 17 / One UI 9 system image.

**Status:** configuration/preflight only. This repository does **not** currently contain Samsung firmware, a ported ROM, or a flashable build. A successful GitHub Actions preflight is **not** evidence that a ROM boots.

## Roadmap

1. Record the exact stock base build, bootloader revision, donor build and partition map.
2. Obtain firmware lawfully; keep proprietary firmware **out** of public Git history and Actions artifacts.
3. Inspect Android sparse/super partitions, VINTF, SELinux, dynamic-partition sizing and AVB strategy.
4. Implement a separate, source-auditable port pipeline; test packaging offline before flashing.
5. Test recovery and boot, then RIL/data/VoLTE/VoWiFi/brightness and performance on device.

## How to use

Navigate to **Actions → M14 Port Preflight → Run workflow**. Defaults run static checks only. The workflow refuses to claim it built a ROM.

## Upstream attribution

This initial scaffold is independently written and contains no copied ReCoreUI build scripts. If ReCoreUI or other projects' code is incorporated later, preserve their required license/copyright notices and document upstream sources.

**Warning:** unlocking/flashing can erase data or prevent boot. Back up data and confirm recovery/stock restore steps before any on-device tests.
