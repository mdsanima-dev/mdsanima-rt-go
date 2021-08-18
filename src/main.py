"""
Main application MDSANIMA-RT-GO
"""


from __init__ import __version__

import kivy
kivy.require('2.0.0')

import os
import sys
from datetime import datetime

from config import windows
from config.image import get_images
from config.setting import check_platform, theme_kivy

from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton, MDIconButton
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.slider import MDSlider
from kivymd.uix.textfield import MDTextField
from plyer import notification


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


class MDSRTGO_scr_1(Screen):
    """
    Welcome first screen change with timer to seconde screen main.

    :param Screen: screen class kivy
    :type Screen: class
    """
    def __init__(self, **kwargs):
        super(MDSRTGO_scr_1, self).__init__(**kwargs)
        layout = MDFloatLayout()
        img = get_images()

        mdsanima_rt_go = (
            'MDSANIMA RT GO '
            + '[b][color=#329EF4]'
            + 'v' + str(__version__)
            + '[/color][/b]')

        bacground = Image(
            source=resource_path(img[1]), size=self.size, pos=self.pos,
            size_hint_y=None, size_hint_x=None,
            height='1849sp', width='1075sp',
            pos_hint={'center_x':0.5, 'center_y':0.5},
            allow_stretch=True)

        btn_go_rendering = MDFlatButton(
            text='GO RENDERING!', on_press=self.screen_switch,
            pos_hint={'center_x':0.5, 'center_y':0.6},
            font_size='35')

        btn_logo_mdsanima = MDIconButton(
            icon=resource_path(img[3]), on_press=self.screen_switch,
            user_font_size='80', size_hint_y=None,
            pos_hint={'center_x':0.5, 'center_y':0.5})

        lbl_click_me = MDLabel(
            text='CLICK ME!', halign='center',
            pos_hint={'center_x':0.5, 'center_y':0.57},
            font_style='Caption',
            theme_text_color='Secondary')

        lbl_info_version = MDLabel(
            text=mdsanima_rt_go,
            halign='center',
            pos_hint={'center_x':0.5, 'center_y':0.02},
            font_style='Caption',
            theme_text_color='Secondary',
            markup=True)

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
    """
    Main second screen render time calculation.

    :param Screen: screen class kivy
    :type Screen: class
    """
    def __init__(self, **kwargs):
        super(MDSRTGO_scr_2, self).__init__(**kwargs)
        layout = MDFloatLayout()
        img = get_images()

        layout_box = MDBoxLayout(
            orientation='vertical',
            padding=0, spacing=0,
            size_hint_x=1, size_hint_y=0.3,
            pos_hint={'center_x':0.5, 'top':0.8})

        mdsanima_rt_go = (
            'MDSANIMA RT GO '
            + '[b][color=#329EF4]'
            + 'v' + str(__version__)
            + '[/color][/b]')

        bacground = Image(
            source=resource_path(img[2]), size=self.size, pos=self.pos,
            size_hint_y=None, size_hint_x=None,
            height='1849sp', width='1075sp',
            pos_hint={'center_x':0.5, 'center_y':0.5},
            allow_stretch=True)

        lbl_top_name = MDLabel(
            text='RENDER TIME CALCULATOR',
            halign='center',
            pos_hint={'center_x':0.5, 'center_y':0.96},
            font_style='H6',
            theme_text_color='Primary',
            markup=True)

        tfl_how_many_frame = MDTextField(
            required=True,
            hint_text='NUMBER OF FRAMES',
            helper_text_mode='on_error',
            input_filter='int', max_text_length=6,
            pos_hint={'center_x':0.5, 'center_y':0.9},
            size_hint_x=0.85)

        lbl_render_frame = MDLabel(
            text='RENDER TIME ONE FRAME',
            halign='left',
            size_hint=(None,None), size=(170,40),
            pos_hint={'center_x':0.24, 'center_y':0.84},
            font_style='Body2',
            theme_text_color='Hint')

        lbl_hours = MDLabel(
            text='HOURS:',
            halign='right',
            size_hint=(None,None), size=(70,40),
            pos_hint={'center_x':0.2, 'center_y':0.8},
            font_style='Button',
            theme_text_color='Secondary')

        lbl_minutes = MDLabel(
            text='MINUTES:',
            halign='right',
            size_hint=(None,None), size=(70,40),
            pos_hint={'center_x':0.2, 'center_y':0.7},
            font_style='Button',
            theme_text_color='Secondary')

        lbl_seconds = MDLabel(
            text='SECONDS:',
            halign='right',
            size_hint=(None,None), size=(70,40),
            pos_hint={'center_x':0.2, 'center_y':0.6},
            font_style='Button',
            theme_text_color='Secondary')

        lbl_hours_val = MDLabel(
            text='0',
            halign='right',
            size_hint=(None,None), size=(70,40),
            pos_hint={'center_x':0.23, 'center_y':0.8},
            font_style='Button',
            theme_text_color='Error')

        lbl_minutes_val = MDLabel(
            text='0',
            halign='right',
            size_hint=(None,None), size=(70,40),
            pos_hint={'center_x':0.23, 'center_y':0.7},
            font_style='Button',
            theme_text_color='Error')

        lbl_seconds_val = MDLabel(
            text='0',
            halign='right',
            size_hint=(None,None), size=(70,40),
            pos_hint={'center_x':0.23, 'center_y':0.6},
            font_style='Button',
            theme_text_color='Error')

        sld_hours_val = MDSlider(
            min=0, max=24, value=0,
            pos_hint={'center_x':0.5, 'center_y':0.78},
            size_hint_x=0.75,
            color='#7c7c7c')

        sld_minutes_val = MDSlider(
            min=0, max=60, value=0,
            pos_hint={'center_x':0.5, 'center_y':0.68},
            size_hint_x=0.75,
            color='#7c7c7c')

        sld_seconds_val = MDSlider(
            min=0, max=60, value=0,
            pos_hint={'center_x':0.5, 'center_y':0.58},
            size_hint_x=0.75,
            color='#7c7c7c')

        lbl_render_time = MDLabel(
            text='RENDER TIME',
            halign='left',
            size_hint=(None,None), size=(170,40),
            pos_hint={'center_x':0.24, 'center_y':0.48},
            font_style='Body2',
            theme_text_color='Hint')

        lbl_render_start = MDLabel(
            text='START RENDER',
            halign='left',
            size_hint=(None,None), size=(170,40),
            pos_hint={'center_x':0.24, 'center_y':0.38},
            font_style='Body2',
            theme_text_color='Hint')

        lbl_render_finish = MDLabel(
            text='FINISH RENDER',
            halign='left',
            size_hint=(None,None), size=(170,40),
            pos_hint={'center_x':0.24, 'center_y':0.28},
            font_style='Body2',
            theme_text_color='Hint')

        lbl_render_time_val = MDLabel(
            text='10 minutes',
            halign='left',
            size_hint=(None,None), size=(450,40),
            pos_hint={'center_x':0.515, 'center_y':0.44},
            font_style='H5',
            theme_text_color='Custom',
            text_color = [.2510,.5529,.9765,1])

        lbl_render_start_val = MDLabel(
            text='2021-08-18  23:43:44  Wednesday',
            halign='left',
            size_hint=(None,None), size=(450,40),
            pos_hint={'center_x':0.515, 'center_y':0.34},
            font_style='H6',
            theme_text_color='Secondary')

        lbl_render_finish_val = MDLabel(
            text='2021-08-18  23:53:44  Wednesday',
            halign='left',
            size_hint=(None,None), size=(450,40),
            pos_hint={'center_x':0.515, 'center_y':0.24},
            font_style='H6',
            theme_text_color='Secondary')

        btn_app_info = MDFlatButton(
            text='app info', size_hint=(None,None), size=(101,40),
            pos_hint={'x':0.416,'y':0.03},
            on_release=self.screen_switch)

        lbl_info_version = MDLabel(
            text=mdsanima_rt_go,
            halign='center',
            pos_hint={'center_x':0.5, 'center_y':0.02},
            font_style='Caption',
            theme_text_color='Secondary',
            markup=True)

        # add widget layout
        layout.add_widget(bacground)

        layout.add_widget(lbl_top_name)
        layout.add_widget(tfl_how_many_frame)

        layout.add_widget(lbl_render_frame)

        layout.add_widget(lbl_hours)
        layout.add_widget(lbl_hours_val)
        layout_box.add_widget(sld_hours_val)

        layout.add_widget(lbl_minutes)
        layout.add_widget(lbl_minutes_val)
        layout_box.add_widget(sld_minutes_val)

        layout.add_widget(lbl_seconds)
        layout.add_widget(lbl_seconds_val)
        layout_box.add_widget(sld_seconds_val)

        layout.add_widget(lbl_render_time)
        layout.add_widget(lbl_render_time_val)

        layout.add_widget(lbl_render_start)
        layout.add_widget(lbl_render_start_val)

        layout.add_widget(lbl_render_finish)
        layout.add_widget(lbl_render_finish_val)

        layout.add_widget(btn_app_info)
        layout.add_widget(lbl_info_version)

        # draw all widget
        self.add_widget(layout)
        self.add_widget(layout_box)

    def screen_switch(self, instance):
        self.manager.current = 'scr_3'
        self.manager.transition.direction = 'up'


class MDSRTGO_scr_3(Screen):
    def __init__(self, **kwargs):
        super(MDSRTGO_scr_3, self).__init__(**kwargs)
        layout = MDFloatLayout()
        btn = Button(text='SCREEN 1', on_release=self.screen_switch)

        layout.add_widget(btn)
        self.add_widget(layout)

    def screen_switch(self, instance):
        self.manager.current = 'scr_2'
        self.manager.transition.direction = 'right'


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
            timeout=10)
        sm = ScreenManager()
        sm.add_widget(MDSRTGO_scr_1(name='scr_1'))
        sm.add_widget(MDSRTGO_scr_2(name='scr_2'))
        sm.add_widget(MDSRTGO_scr_3(name='scr_3'))
        return sm


if __name__ == '__main__':
    MDSRTGO_main().run()
