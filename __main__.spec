# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['project\\__main__.py'],
    pathex=[],
    binaries=[],
    datas=[("project\plant_database.db", ".")],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='Plantfolio',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    icon="Plantfolio_logo_small.ico",
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
