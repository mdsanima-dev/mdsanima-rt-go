# -*- mode: python ; coding: utf-8 -*-
#from kivy_deps import sdl2
from plyer import notification
from kivymd import hooks_path as kivymd_hooks_path
#from kivy.tools.packaging.pyinstaller_hooks import get_deps_all, hookspath, runtime_hooks

from src.__init__ import __version__

block_cipher = None

a = Analysis(['src/main.py'],
            pathex=['/media/sf_mdsanima-rt-go/src/'],
            binaries=[],
            datas=[],
            hiddenimports=[
                'plyer.platforms.linux.notification',
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
                #'PIL',
                'cryptography',
                'lib2to3',
                'win32com'
                ],
            win_no_prefer_redirects=False,
            win_private_assemblies=False,
            cipher=block_cipher,
            noarchive=False
            #**get_deps_all()
            )

#a.binaries = [x for x in a.binaries if not
#                os.path.dirname(x[1]).startswith('C:\\Windows\\system32')
#                ]

a.exclude_system_libraries(list_of_exceptions=['libexpat*', '*krb*'])

pyz = PYZ(a.pure, a.zipped_data,
            cipher=block_cipher
            )

exe = EXE(pyz,
            a.scripts + [('O','','OPTION')],
            a.binaries + [('O','','OPTION')],
            a.zipfiles + [('O','','OPTION')],
            a.datas + [
                ('image/ic_launcher/res/mipmap-hdpi/ic_launcher.png', '/media/sf_mdsanima-rt-go/src/image/ic_launcher/res/mipmap-hdpi/ic_launcher.png', 'DATA'),
                ('image/ic_launcher/res/mipmap-hdpi/ic_launcher.ico', '/media/sf_mdsanima-rt-go/src/image/ic_launcher/res/mipmap-hdpi/ic_launcher.ico', 'DATA'),
                ('image/ic_launcher/res/mipmap-xxxhdpi/ic_launcher.png', '/media/sf_mdsanima-rt-go/src/image/ic_launcher/res/mipmap-xxxhdpi/ic_launcher.png', 'DATA'),
                ('image/ic_launcher/res/mipmap-xxxhdpi/ic_launcher.ico', '/media/sf_mdsanima-rt-go/src/image/ic_launcher/res/mipmap-xxxhdpi/ic_launcher.ico', 'DATA'),
                ('image/background/bg_1.png', '/media/sf_mdsanima-rt-go/src/image/background/bg_1.png', 'DATA'),
                ('image/background/bg_2.png', '/media/sf_mdsanima-rt-go/src/image/background/bg_2.png', 'DATA'),
                ('image/ic_launcher/icons/ic_mdsanima_12_drp_sdw_w.png', '/media/sf_mdsanima-rt-go/src/image/ic_launcher/icons/ic_mdsanima_12_drp_sdw_w.png', 'DATA'),
                ('image/ic_launcher/icons/ic_mdsanima_20_drp_sdw_b.png', '/media/sf_mdsanima-rt-go/src/image/ic_launcher/icons/ic_mdsanima_20_drp_sdw_b.png', 'DATA'),
                ('image/ic_launcher/ascii_mdsanima.png', '/media/sf_mdsanima-rt-go/src/image/ic_launcher/ascii_mdsanima.png', 'DATA')
                ],
            [],
            exclude_binaries=False,
            name=("mdsanima-rt-go-" + str(__version__) + "-linux64-debug"),
            debug=True,
            bootloader_ignore_signals=False,
            #*[Tree(p) for p in (sdl2.dep_bins)],
            strip=False,
            upx=True,
	        upx_exclude=[],
	        runtime_tmpdir=None,
            console=True,
            icon='/media/sf_mdsanima-rt-go/src/image/ic_launcher/res/mipmap-hdpi/ic_launcher.ico'
            )
