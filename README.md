# mdsanima-rt-go

Cross Platform Application for Calculating Render Time.

## Requirement

Run this command in `wsl-1` and `PowerShell` on the `Windows 10`:

```shell
python3.8 -m pip install kivy==2.0.0
python3.8 -m pip install kivymd==0.104.2
python3.8 -m pip install pyinstaller==4.5.1
```

## Run `standard-version`

First run `standard-version` on `wsl` to generate `changelog.md` and bumping
verion in `__init__.py` and `spec_windows_version.rc` files:

```shell
standard-version --skip.commit --skip.tag
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
sudo python3.8 -m PyInstaller --distpath /media/sf_mdsanima-rt-go/dist/linux --workpath /media/sf_mdsanima-rt-go/.build --onefile /media/sf_mdsanima-rt-go/spec_linux_onefile.spec
```
