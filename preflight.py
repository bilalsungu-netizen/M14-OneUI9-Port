#!/usr/bin/env python3
"""Validate project metadata. Never builds or modifies firmware."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
config = json.loads((ROOT / 'config' / 'device.json').read_text(encoding='utf-8'))
assert config['device'] == 'm14x', 'Unexpected device codename'
assert config['model'] == 'SM-M146B', 'Unexpected device model'
assert config['target_android'] == 17
assert config['target_one_ui'] == '9.0'
assert config['port_status'] == 'preflight-only'
for key in ('stock_firmware', 'stock_bootloader_revision', 'donor_model', 'donor_firmware'):
    value = config[key]
    assert value is None or isinstance(value, (str, int)), f'Invalid {key}'
    print(f'{key}: {value if value is not None else "NOT SET"}')
print('PASS: project metadata is valid.')
print('NO ROM WAS BUILT; DONOR FIRMWARE AND DEVICE COMPATIBILITY REMAIN UNVERIFIED.')
