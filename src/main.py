"""
Main application MDSANIMA RT GO
"""


import kivy

from __init__ import __version__

kivy.require('2.0.0')

from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from plyer import notification

from __init__ import resource_path
from config.image import get_images
from config.setting import check_platform, theme_kivy
from libs.screen.calculation import MDSRTGO_scr_2
from libs.screen.info import MDSRTGO_scr_3
from libs.screen.welcome import MDSRTGO_scr_1


class MDSRTGO_main(MDApp):
    title = 'MDSANIMA RT GO v' + __version__
    def build(self):
        theme_kivy(self, 'Orange', 'Blue', 'Dark')

        img = get_images()
        self.icon = resource_path(img[0])

        notification_icon = check_platform()
        notification.notify(
            title='MDSANIMA RT GO',
            message='You have a 2 messages and 10 new issues',
            app_name='MDSANIMA RT GO',
            app_icon=resource_path(notification_icon),
            timeout=10
        )

        sm = ScreenManager()
        sm.add_widget(MDSRTGO_scr_1(name='scr_1'))
        sm.add_widget(MDSRTGO_scr_2(name='scr_2'))
        sm.add_widget(MDSRTGO_scr_3(name='scr_3'))

        return sm


if __name__ == '__main__':
    MDSRTGO_main().run()
