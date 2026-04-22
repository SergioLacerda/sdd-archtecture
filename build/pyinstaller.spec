#!/usr/bin/env python3
# -*- mode: python ; coding: utf-8 -*-
"""PyInstaller build specification for SDD CLI."""

block_cipher = None

a = Analysis(
    ['../sdd_cli/__main__.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[
        'typer',
        'click',
        'rich',
        'msgpack',
        'yaml',
        'sdd_wizard',
        'sdd_wizard.governance_runtime_loader',
        'sdd_wizard.wizard_integrator',
        'sdd_wizard.customization_template_generator',
        'sdd_wizard.wizard_orchestrator',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludedimports=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='sdd',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
