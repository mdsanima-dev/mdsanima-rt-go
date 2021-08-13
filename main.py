"""
Main application MDSANIMA-RT-GO
"""


from __init__ import __version__

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
from kivy.utils import platform


# checking platform and print message
if platform == 'win':
    print('hello from windows')
if platform == 'linux':
    print('hello from linux')
if platform == 'android':
    print('hello from android')
if platform == 'macosx':
    print('hello from macosx')
if platform == 'ios':
    print('hello from ios')
if platform == 'unknown':
    print('hello from unknown')


class MDSRTGO_scr_1(Screen):
    def __init__(self, **kwargs):
        super(MDSRTGO_scr_1, self).__init__(**kwargs)
        layout = FloatLayout()
        btn = Button(text='SCREEN 2', on_release=self.screen_switch)

        layout.add_widget(btn)
        self.add_widget(layout)

    def screen_switch(self, instance):
        self.manager.current = 'scr_2'
        self.manager.transition.direction = 'left'


class MDSRTGO_scr_2(Screen):
    def __init__(self, **kwargs):
        super(MDSRTGO_scr_2, self).__init__(**kwargs)
        layout = FloatLayout()
        btn = Button(text='SCREEN 3', on_release=self.screen_switch)

        layout.add_widget(btn)
        self.add_widget(layout)

    def screen_switch(self, instance):
        self.manager.current = 'scr_3'
        self.manager.transition.direction = 'left'


class MDSRTGO_scr_3(Screen):
    def __init__(self, **kwargs):
        super(MDSRTGO_scr_3, self).__init__(**kwargs)
        layout = FloatLayout()
        btn = Button(text='SCREEN 1', on_release=self.screen_switch)

        layout.add_widget(btn)
        self.add_widget(layout)

    def screen_switch(self, instance):
        self.manager.current = 'scr_1'
        self.manager.transition.direction = 'right'


class MDSRTGO_main(MDApp):
    title = "MDSANIMA RT GO v" + __version__
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MDSRTGO_scr_1(name='scr_1'))
        sm.add_widget(MDSRTGO_scr_2(name='scr_2'))
        sm.add_widget(MDSRTGO_scr_3(name='scr_3'))
        return sm


if __name__ == "__main__":
    MDSRTGO_main().run()