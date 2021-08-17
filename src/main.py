"""
Main application MDSANIMA-RT-GO
"""


from __init__ import __version__

import kivy
kivy.require('2.0.0')
import config.windows

from config.setting import check_platform, theme_kivy
from config.image import get_images
from datetime import datetime
from kivymd.app import MDApp
from kivymd.uix.button import MDIconButton, MDFlatButton
from kivymd.uix.label import MDLabel
from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen, ScreenManager
from plyer import notification


class MDSRTGO_scr_1(Screen):
    def __init__(self, **kwargs):
        super(MDSRTGO_scr_1, self).__init__(**kwargs)
        layout = FloatLayout()
        img = get_images()

        mdsanima_rt_go = (
            "MDSANIMA RT GO "
            + '[b][color=#329EF4]'
            + "v" + str(__version__)
            + '[/color][/b]')

        bacground = Image(
            source=img[1], size=self.size, pos=self.pos,
            size_hint_y=None, size_hint_x=None,
            height='1849sp', width='1075sp',
            pos_hint={'center_x':.5, 'center_y':.5},
            allow_stretch=True)

        btn_go_rendering = MDFlatButton(
            text="GO RENDERING!", on_press=self.screen_switch,
            pos_hint = {'center_x':.5, 'center_y':.6},
            font_size = "35")

        btn_logo_mdsanima = MDIconButton(
            icon=img[3], on_press=self.screen_switch,
            user_font_size="80", size_hint_y=None,
            pos_hint={'center_x':.5, 'center_y':.5})

        lbl_click_me = MDLabel(
            text="CLICK ME!", halign="center",
            pos_hint={'center_x':.5, 'center_y':.57},
            font_style="Caption",
            theme_text_color='Secondary')

        lbl_info_version = MDLabel(
            text = mdsanima_rt_go,
            halign = "center",
            pos_hint = {'center_x':.5, 'center_y':.02},
            font_style = "Caption",
            theme_text_color = 'Secondary',
            markup = True
            )

        # add widget layout
        layout.add_widget(bacground)
        layout.add_widget(btn_go_rendering)
        layout.add_widget(btn_logo_mdsanima)
        layout.add_widget(lbl_click_me)
        layout.add_widget(lbl_info_version)

        # draw all widget
        self.add_widget(layout)

        # switch screen after 30 seconds
        Clock.schedule_once(self.clk_screen, 30)

    def screen_switch(self, instance):
        self.manager.current = 'scr_2'
        self.manager.transition.direction = 'left'

    def screen_switch_clk(self, instance):
        if (self.manager.current == 'scr_1'):
            self.manager.current = 'scr_2'
            self.manager.transition.direction = 'left'
        else:
            pass

    def clk_screen(self, dt):
        time_clk = datetime.now()
        self.screen_switch_clk(time_clk)


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
        theme_kivy(self, 'Orange', 'Blue', 'Dark')
        img = get_images()
        self.icon = img[0]
        notification_icon = check_platform()
        notification.notify(
            title="MDSANIMA RT GO",
            message="You have a 2 messages and 10 new issues",
            app_name="MDSANIMA RT GO",
            app_icon=notification_icon,
            timeout=10)
        sm = ScreenManager()
        sm.add_widget(MDSRTGO_scr_1(name='scr_1'))
        sm.add_widget(MDSRTGO_scr_2(name='scr_2'))
        sm.add_widget(MDSRTGO_scr_3(name='scr_3'))
        return sm


if __name__ == "__main__":
    MDSRTGO_main().run()
