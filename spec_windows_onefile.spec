# -*- mode: python ; coding: utf-8 -*-
from kivy_deps import sdl2
from plyer import notification
from kivymd import hooks_path as kivymd_hooks_path

from __init__ import __version__

block_cipher = None

a = Analysis(['main.py'],
            pathex=['J:\\github-mdsanima-dev\\mdsanima-rt-go'],
            binaries=[],
            datas=[],
            hiddenimports=[
                'plyer.platforms.win.notification',
                'kivymd.uix.toolbar',
                'kivymd.icon_definitions',
                'kivymd.icon_definitions.md_icons',
                'kivymd.uix.label',
                'kivymd.uix.navigationdrawer',
                'kivymd.uix.list'
                ],
            hookspath=[kivymd_hooks_path],
            runtime_hooks=[],
            excludes=[
                'cv2',
                'enchant',
                'docutils',
                'grpc',
                'numpy',
                'PIL',
                'cryptography',
                'lib2to3',
                'win32com'
                ],
            win_no_prefer_redirects=False,
            win_private_assemblies=False,
            cipher=block_cipher,
            noarchive=False
            )

a.binaries = [x for x in a.binaries if not
              os.path.dirname(x[1]).startswith('C:\\Windows\\system32')]

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
            a.scripts + [('O','','OPTION')],
            a.binaries + [('O','','OPTION')],
            a.zipfiles + [('O','','OPTION')],
            a.datas + [
                ('image/ic_launcher/res/mipmap-hdpi/ic_launcher.png', 'J:\\github-mdsanima-dev\\mdsanima-rt-go\\image\\ic_launcher\\res\\mipmap-hdpi\\ic_launcher.png', 'DATA'),
                ('image/ic_launcher/res/mipmap-xxxhdpi/ic_launcher.png', 'J:\\github-mdsanima-dev\\mdsanima-rt-go\\image\\ic_launcher\\res\\mipmap-xxxhdpi\\ic_launcher.png', 'DATA'),
                ('image/ic_launcher/res/mipmap-xxxhdpi/ic_launcher.ico', 'J:\\github-mdsanima-dev\\mdsanima-rt-go\\image\\ic_launcher\\res\\mipmap-xxxhdpi\\ic_launcher.ico', 'DATA')
                ],
            [],
            name=("mdsanima-rt-go-" + str(__version__) + "-windows64-debug"),
            debug=True,
            bootloader_ignore_signals=False,
            *[Tree(p) for p in (sdl2.dep_bins)],
            strip=False,
            upx=True,
	        upx_exclude=[],
	        runtime_tmpdir=None,
            console=True , icon='J:\\github-mdsanima-dev\\mdsanima-rt-go\\image\\ic_launcher\\res\\mipmap-xxxhdpi\\ic_launcher.ico',
            version='J:\\github-mdsanima-dev\\mdsanima-rt-go\\spec_windows_version.rc')
