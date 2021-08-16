#!/usr/bin/python3

"""
Help Developmend Release Workflow.

.. important::

    This file is not a part of `mdsanima-rt-go` App.
    Run in `package.json` script.

First step: Bumping version in `package.json` file with `standard-version`
Bumping version in `__init__.py` file.
Bumping version in `spec_windows_version.rc` file.
Autogenerate `CHANGELOG.md` based on commits.
Committing this file with signed GPG keys.
Creating tagging release and signed commit with GPG keys.

Check version in `package.json` and then replece this version in `__init__.py`
file and `spec_windows_version.rc`.

:usage: ./make_release.py
"""


import os
import json
import pathlib

HERE = pathlib.Path(__file__).parent


def go_check():
    """
    Load data from `package.json`file.
    Run in `package.json` script `postbump` executex after the version
    is bumped.

    :return: new version to replece
    :rtype: str
    """
    path_to_file = HERE / "package.json"
    with open(path_to_file) as dt:
        data_package = json.load(dt)
    new_version = data_package["version"]
    return new_version


def go_read_write(bump_file, old_version, new_version):
    """
    This function replecing old version with new version.

    :param bump_file: file to bump `__init__.py` or `spec_windows_version.rc`
    :type bump_file: str
    :param old_version: lines with old version
    :type old_version: str
    :param new_version: lines with new version
    :type new_version: str
    """
    path_to_file = HERE / bump_file
    with open(path_to_file, 'r', encoding='utf-8') as r:
        replace_version = r.read().replace(old_version, new_version)
    with open(path_to_file, 'w', encoding='utf-8') as w:
        w.write(replace_version)


def go_bump_init():
    """
    Reading file `__init__.py` and splits lines. Searching matching lines
    and replacing this line with new version. Printing info in the console.
    """
    path_to_file = HERE / "src/__init__.py"
    with open(path_to_file, 'r', encoding='utf-8') as r:
        lines = r.read().splitlines()
    lines_len = len(lines)

    for line in range(lines_len):
        if str("__version__") in str(lines[line]):
            print('[MDSANIMA-DEV] -> bumping __init__.py')
            print('[MDSANIMA-DEV] => matching line', line + 1, lines[line])
            new_version = go_check()
            print('[MDSANIMA-DEV] => checking new version =>', new_version)
            new_line_versi = '__version__ = "' + new_version + '"'
            go_read_write(
                'src/__init__.py', str(lines[line]), str(new_line_versi)
                )
            print('[MDSANIMA-DEV] => replace line', line + 1, new_line_versi)


def go_bump_rc():
    """
    Reading file `spec_windows_version.rc` and splits lines. Searching matching
    lines and replacing this line with new version. Printing info in the
    console.
    """
    # check new version and split
    new_version = go_check()
    split_new_versi = str(new_version).rsplit(".")

    # initial variable new version major minor path
    new_MAJOR = str(split_new_versi[0])
    new_MINOR = str(split_new_versi[1])
    new_PATCH = str(split_new_versi[2])

    # initial variable new version
    new_version = str(new_MAJOR + '.' + new_MINOR + '.' + new_PATCH)

    # initial variable lines to replacing new version
    new_line_09 = "    filevers=(" + new_MAJOR + ", " + new_MINOR + ", " + new_PATCH + ", 0),"
    new_line_10 = "    prodvers=(" + new_MAJOR + ", " + new_MINOR + ", " + new_PATCH + ", 0),"
    new_line_34 = "        StringStruct(u'FileVersion', u'" + new_version + "'),"
    new_line_39 = "        StringStruct(u'ProductVersion', u'" + new_version + "')])"

    # print info
    print('[MDSANIMA-DEV] -> bumping spec_windows_version.rc')

    # file to bump
    path_to_file = HERE / "spec_windows_version.rc"
    with open(path_to_file, 'r', encoding='utf-8') as r:
        lines = r.read().splitlines()
    lines_len = len(lines)

    # find matching lines and replace with new version
    for line in range(lines_len):
        if line + 1 == 9:
            old_lines = lines[line]
            go_read_write(path_to_file, old_lines, new_line_09)
        if line + 1 == 10:
            old_lines = lines[line]
            go_read_write(path_to_file, old_lines, new_line_10)
        if line + 1 == 34:
            old_lines = lines[line]
            go_read_write(path_to_file, old_lines, new_line_34)
        if line + 1 == 39:
            old_lines = lines[line]
            go_read_write(path_to_file, old_lines, new_line_39)

    # print info
    print('[MDSANIMA-DEV] => replace line for new version done', new_version)


if __name__ == "__main__":
    go_bump_init()
    go_bump_rc()
