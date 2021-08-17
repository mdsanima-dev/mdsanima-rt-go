"""
Base Kivy Settings
"""


from kivymd.theming import ThemeManager
from kivy.utils import platform
from utils.resource import resource_path


def theme_kivy(
    self,
    primary_pallete='Gray',
    accent_pallete='Blue',
    theme_style='Dark',
    primary_dark_hue='A700'
    ):
    self.theme_cls = ThemeManager()
    self.theme_cls.primary_palette = primary_pallete
    self.theme_cls.accent_pallete = accent_pallete
    self.theme_cls.theme_style = theme_style
    self.theme_cls.primary_dark_hue = primary_dark_hue


def check_platform():
    path = '../image/ic_launcher/res/mipmap-xxxhdpi/'
    if platform == 'win':
        print('hello from windows')
        notyfication_icon = resource_path(path + 'ic_launcher.ico')
    if platform == 'linux':
        print('hello from linux')
        notyfication_icon = resource_path(path + 'ic_launcher.png')
    if platform == 'android':
        print('hello from android')
        notyfication_icon = resource_path(path + 'ic_launcher.png')
    if platform == 'macosx':
        print('hello from macosx')
        notyfication_icon = resource_path(path + 'ic_launcher.png')
    if platform == 'ios':
        print('hello from ios')
        notyfication_icon = resource_path(path + 'ic_launcher.png')
    if platform == 'unknown':
        print('hello from unknown')
        notyfication_icon = resource_path(path + 'ic_launcher.png')
    return notyfication_icon
