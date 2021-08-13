"""
Main application MDSANIMA-RT-GO
"""


from . import __version__

import kivy
kivy.require('2.0.0')

from kivy import Config


# set configuration windows
Config.set('graphics', 'width', '500')
Config.set('graphics', 'height', '860')
Config.set('graphics', 'minimum_width', '500')
Config.set('graphics', 'minimum_height', '600')
Config.set('graphics', 'resizable', False)


from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen, ScreenManager


class MDSRTGO_scr_1(Screen):
    def __init__(self, **kwargs):
        super(MDSRTGO_scr_1, self).__init__(**kwargs)
        pass


class MDSRTGO_scr_2(Screen):
    def __init__(self, **kwargs):
        super(MDSRTGO_scr_2, self).__init__(**kwargs)
        pass


class MDSRTGO_scr_3(Screen):
    def __init__(self, **kwargs):
        super(MDSRTGO_scr_3, self).__init__(**kwargs)
        pass


class MDSRTGO_main(MDApp):
    def build(self):
        pass


if __name__ == "__main__":
    MDSRTGO_main().run()
