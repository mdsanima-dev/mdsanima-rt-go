__version__ = "0.3.0"


import os
import sys


def resource_path(relative_path: str):
    """
    Create path on the file in all platform build.

    :param relative_path: wher file is stored
    :type relative_path: str
    :return: resource path on platform build
    :rtype: path
    """
    base_path = getattr(
        sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)
