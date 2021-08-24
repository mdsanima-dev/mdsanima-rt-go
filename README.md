# mdsanima-rt-go

![GitHub issues](https://img.shields.io/github/issues-raw/mdsanima-dev/mdsanima-rt-go?style=flat)
![GitHub closed issues](https://img.shields.io/github/issues-closed/mdsanima-dev/mdsanima-rt-go?style=flat)
![GitHub](https://img.shields.io/github/license/mdsanima-dev/mdsanima-rt-go?style=flat)
![Lines of code](https://img.shields.io/tokei/lines/github/mdsanima-dev/mdsanima-rt-go?style=flat)
![GitHub top language](https://img.shields.io/github/languages/top/mdsanima-dev/mdsanima-rt-go)

Cross Platform Application for Calculating Render Time.

## Testing

This is a base application build on `Windows` `Android` and `Linux`.

All build is a debug mode.
This is a not production build only for testing.

`Linux Ubuntu 20.04`

<img width="960" alt="mdsanima rt go-0 2 0-linux64-debug" src="https://user-images.githubusercontent.com/3817871/129733143-f477b77e-dfce-4ebc-8dd9-a7f67bd8df22.png">

`Microsoft Windows 10`

<img width="960" alt="mdsanima rt go-0 2 0-windows64-debug" src="https://user-images.githubusercontent.com/3817871/129733177-bb7ced9c-cebf-42f8-b3a2-d6b295510ead.png">

`Samsung S7 Edge Android armeabi-v7a`

| ![mdsanimartgo-020-armeabi-v7a-debug_samsung_s7edge_splash][1] | ![mdsanimartgo-020-armeabi-v7a-debug_samsung_s7edge_main][2] | ![omdsanimartgo-020-armeabi-v7a-debug_samsung_s7edge_notification][3] |
|---|---|---|

[1]: https://user-images.githubusercontent.com/3817871/129733791-6a784e94-fdd2-4231-89e1-e1484baa6108.jpg
[2]: https://user-images.githubusercontent.com/3817871/129733777-17447d63-a9a3-4aa5-9337-2a9a748b17e2.jpg
[3]: https://user-images.githubusercontent.com/3817871/129733669-04e80fd7-60f8-4932-985b-030ca1bde9e8.jpg

## Requirement

Run this command in **wsl-1** and **PowerShell** on the `Windows 10`:

```shell
python3.8 -m pip install -r requirements.txt
```

If kivy does not detect opengl add this code to `setting.py`:

```python
import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
```

## Run `standard-version`

First run **standard-version** on **wsl** to generate `CHANGELOG.md`
and bumping verion in `__init__.py` and `spec_windows_version.rc` files:

```shell
standard-version --skip.commit --skip.tag
```

Only bump release as minor and check:

```shell
standard-version --skip.changelog --skip.commit --skip.tag --release-as minor --dry-run
```

Add bumping files and commiting:

```shell
git add . && git commit -m "chore(release): 0.1.0"
```

Create tag:

```shell
standard-version --skip.bump --skip.changelog --commit-all --sign
```

## Build Windows `.exe`

Run on `PowerShell` in Windows:

```PowerShell
cd J:\github-mdsanima-dev\mdsanima-rt-go
.\spec_windows_build.cmd
```

## Build Linux

Run on `shell` in `ubuntu_20_04` Virtual Box:

```shell
sudo su
cd /media/sf_mdsanima-rt-go
sudo python3.8 -m PyInstaller \
    --distpath /media/sf_mdsanima-rt-go/dist/linux \
    --workpath /media/sf_mdsanima-rt-go/.build \
    --onefile /media/sf_mdsanima-rt-go/spec_linux_onefile.spec
```

## Build Android `armeabi-v7a` `arm64-v8a` `x86` `x86_64`

Connect phone to pc and run on `PowerShell` this command:

```PowerShell
cd C:\adb
.\adb.exe devices
```

If List of devices attached is empty run thic command:

```PowerShell
.\adb.exe kill-server
.\adb.exe devices
```

Now shuld show devices

Run this on `wsl` to copy all files in to `home` directory:

```shell
cd /home/mdsanima/mdsanima-rt-go/
rm -r * && cp -r /mnt/j/github-mdsanima-dev/mdsanima-rt-go/* .
```

Before building if requirements on buildozer.spec updated:

```shell
sudo buildozer android clean
```

Build and deploy:

```shell
sudo buildozer --profile armeabi-v7a -v android debug deploy run logcat
sudo buildozer --profile arm64-v8a -v android debug
sudo buildozer --profile x86 -v android debug
sudo buildozer --profile x86_64 -v android debug
```

Adb install:

```shell
adb install -r /home/mdsanima/mdsanima-rt-go/dist/android/mdsanima.rt.go-0.3.0-armeabi-v7a-debug.apk
```

Copy `.apk` to `dist` folder:

```shell
cp dist/android/mdsanima.rt.go-0.1.0-armeabi-v7a-debug.apk \
    /mnt/j/github-mdsanima-dev/mdsanima-rt-go/dist/android/
```

## Connect With Me

Hi there, I'm Marcin Różewski aka [MDSANIMA](https://mdsanima.com).
These are my social media, check it out please. Thanks.

![GitHub followers](https://img.shields.io/github/followers/mdsanima?style=social)
![Twitter Follow](https://img.shields.io/twitter/follow/toudajew?style=flat-square)
![Twitter Follow](https://img.shields.io/twitter/follow/str9led?style=flat-square)
![Twitter Follow](https://img.shields.io/twitter/follow/mdsanima?style=flat-square)
![YouTube Channel Subscribers](https://img.shields.io/youtube/channel/subscribers/UCB5na2BRwrnwx00LCspbG5Q?style=social)
![YouTube Channel Views](https://img.shields.io/youtube/channel/views/UCB5na2BRwrnwx00LCspbG5Q?style=social)

## License

Cross Platform App `MDSANIMA RT GO` is released under the terms of
[Apache-2.0 License](https://github.com/mdsanima-dev/mdsanima-rt-go/blob/master/LICENSE)
