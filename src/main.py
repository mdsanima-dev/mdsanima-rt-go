"""
Main application MDSANIMA RT GO
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
from kivy.uix.image import Image
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton, MDIconButton
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.list import MDList
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


class MDSRTGO_layout(Screen):
    """
    Class method for `label` or other function when used multiple times.
    """
    def __init__(self, **kwargs):
        super(MDSRTGO_layout, self).__init__(**kwargs)
        pass

    def lbl_info_version(self):
        """
        Label app name and version on the bottom screen.
        """
        mdsanima_rt_go = (
            'MDSANIMA RT GO '
            + '[b][color=#329EF4]'
            + 'v' + str(__version__)
            + '[/color][/b]'
        )
        layout = MDFloatLayout()
        info_version = MDLabel(
            text=mdsanima_rt_go,
            halign='center',
            pos_hint={'center_x':0.5, 'center_y':0.02},
            font_style='Caption',
            theme_text_color='Secondary',
            markup=True
        )
        layout.add_widget(info_version)
        self.add_widget(layout)

    def img_background(self, image: str):
        """
        Background images for screen.

        :param image: path image to use
        :type image: str
        """
        layout = MDFloatLayout()
        background = Image(
            source=resource_path(image), size=self.size, pos=self.pos,
            size_hint_y=None, size_hint_x=None,
            height='1849sp', width='1075sp',
            pos_hint={'center_x':0.5, 'center_y':0.5},
            allow_stretch=True
        )
        layout.add_widget(background)
        self.add_widget(layout)


class MDSRTGO_scr_1(Screen):
    """
    Welcome first screen change with timer to seconde screen main.

    :param Screen: screen class kivy
    :type Screen: class
    """
    def __init__(self, **kwargs):
        super(MDSRTGO_scr_1, self).__init__(**kwargs)
        # assigning function and class to variable
        layout_mds = MDSRTGO_layout()
        layout = MDFloatLayout()
        img = get_images()

        # assigning class to variable
        btn_go_rendering = MDFlatButton(
            text='GO RENDERING!', on_press=self.screen_switch,
            pos_hint={'center_x':0.5, 'center_y':0.6},
            font_size='35'
        )

        btn_logo_mdsanima = MDIconButton(
            icon=resource_path(img[3]), on_press=self.screen_switch,
            user_font_size='80', size_hint_y=None,
            pos_hint={'center_x':0.5, 'center_y':0.5}
        )

        lbl_click_me = MDLabel(
            text='CLICK ME!', halign='center',
            pos_hint={'center_x':0.5, 'center_y':0.57},
            font_style='Caption',
            theme_text_color='Secondary'
        )

        # add widget layout
        layout.add_widget(btn_go_rendering)
        layout.add_widget(btn_logo_mdsanima)
        layout.add_widget(lbl_click_me)

        # draw info version and background
        layout_mds.img_background(img[1])
        layout_mds.lbl_info_version()
        self.add_widget(layout_mds)

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
        # assigning function and class to variable
        layout_mds = MDSRTGO_layout()
        layout = MDFloatLayout()
        img = get_images()

        # assigning class to variable
        lbl_top_name = MDLabel(
            text='RENDER TIME CALCULATOR',
            halign='center',
            size_hint=(None,None), size=(450,40),
            pos_hint={'center_x':0.5, 'center_y':0.96},
            font_style='H5',
            theme_text_color='Primary',
            markup=True
        )

        tfl_how_many_frame = MDTextField(
            required=True,
            hint_text='NUMBER OF FRAMES',
            helper_text_mode='on_error',
            input_filter='int', max_text_length=6,
            pos_hint={'center_x':0.5, 'center_y':0.9},
            size_hint_x=0.85
        )

        lbl_render_frame = MDLabel(
            text='RENDER TIME ONE FRAME',
            halign='left',
            size_hint=(None,None), size=(170,40),
            pos_hint={'center_x':0.24, 'center_y':0.84},
            font_style='Body2',
            theme_text_color='Hint'
        )

        lbl_hours = MDLabel(
            text='HOURS:',
            halign='right',
            size_hint=(None,None), size=(70,40),
            pos_hint={'center_x':0.2, 'center_y':0.8},
            font_style='Button',
            theme_text_color='Secondary'
        )

        lbl_minutes = MDLabel(
            text='MINUTES:',
            halign='right',
            size_hint=(None,None), size=(70,40),
            pos_hint={'center_x':0.2, 'center_y':0.7},
            font_style='Button',
            theme_text_color='Secondary'
        )

        lbl_seconds = MDLabel(
            text='SECONDS:',
            halign='right',
            size_hint=(None,None), size=(70,40),
            pos_hint={'center_x':0.2, 'center_y':0.6},
            font_style='Button',
            theme_text_color='Secondary'
        )

        lbl_hours_val = MDLabel(
            text='0',
            halign='right',
            size_hint=(None,None), size=(70,40),
            pos_hint={'center_x':0.23, 'center_y':0.8},
            font_style='Button',
            theme_text_color='Error'
        )

        lbl_minutes_val = MDLabel(
            text='0',
            halign='right',
            size_hint=(None,None), size=(70,40),
            pos_hint={'center_x':0.23, 'center_y':0.7},
            font_style='Button',
            theme_text_color='Error'
        )

        lbl_seconds_val = MDLabel(
            text='0',
            halign='right',
            size_hint=(None,None), size=(70,40),
            pos_hint={'center_x':0.23, 'center_y':0.6},
            font_style='Button',
            theme_text_color='Error'
        )

        sld_hours_val = MDSlider(
            min=0, max=24, value=0,
            pos_hint={'center_x':0.5, 'center_y':0.78},
            size_hint_x=0.75,
            color='#7c7c7c'
        )

        sld_minutes_val = MDSlider(
            min=0, max=60, value=0,
            pos_hint={'center_x':0.5, 'center_y':0.68},
            size_hint_x=0.75,
            color='#7c7c7c'
        )

        sld_seconds_val = MDSlider(
            min=0, max=60, value=0,
            pos_hint={'center_x':0.5, 'center_y':0.58},
            size_hint_x=0.75,
            color='#7c7c7c'
        )

        lbl_render_time = MDLabel(
            text='RENDER TIME',
            halign='left',
            size_hint=(None,None), size=(170,40),
            pos_hint={'center_x':0.24, 'center_y':0.48},
            font_style='Body2',
            theme_text_color='Hint'
        )

        lbl_render_start = MDLabel(
            text='START RENDER',
            halign='left',
            size_hint=(None,None), size=(170,40),
            pos_hint={'center_x':0.24, 'center_y':0.38},
            font_style='Body2',
            theme_text_color='Hint'
        )

        lbl_render_finish = MDLabel(
            text='FINISH RENDER',
            halign='left',
            size_hint=(None,None), size=(170,40),
            pos_hint={'center_x':0.24, 'center_y':0.28},
            font_style='Body2',
            theme_text_color='Hint'
        )

        lbl_render_time_val = MDLabel(
            text='10 minutes',
            halign='left',
            size_hint=(None,None), size=(450,40),
            pos_hint={'center_x':0.515, 'center_y':0.44},
            font_style='H5',
            theme_text_color='Custom',
            text_color = [.2510,.5529,.9765,1]
        )

        lbl_render_start_val = MDLabel(
            text='2021-08-18  23:43:44  Wednesday',
            halign='left',
            size_hint=(None,None), size=(450,40),
            pos_hint={'center_x':0.515, 'center_y':0.34},
            font_style='H6',
            theme_text_color='Secondary'
        )

        lbl_render_finish_val = MDLabel(
            text='2021-08-18  23:53:44  Wednesday',
            halign='left',
            size_hint=(None,None), size=(450,40),
            pos_hint={'center_x':0.515, 'center_y':0.24},
            font_style='H6',
            theme_text_color='Secondary'
        )

        btn_app_info = MDFlatButton(
            text='APP INFO', size_hint=(None,None), size=(101,40),
            pos_hint={'x':0.416,'y':0.03},
            on_release=self.screen_switch
        )

        layout_box = MDBoxLayout(
            orientation='vertical',
            padding=0, spacing=0,
            size_hint_x=1, size_hint_y=0.3,
            pos_hint={'center_x':0.5, 'top':0.8}
        )

        # add widget layout
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

        # draw info version and background
        layout_mds.img_background(img[2])
        layout_mds.lbl_info_version()
        self.add_widget(layout_mds)

        # draw all widget
        self.add_widget(layout)
        self.add_widget(layout_box)

    def screen_switch(self, instance):
        self.manager.current = 'scr_3'
        self.manager.transition.direction = 'up'


class MDSRTGO_scr_3(Screen):
    """
    Info app screen cover information of the `MDSANIMA RT GO` application.

    :param Screen: screen class kivy
    :type Screen: class
    """
    def __init__(self, **kwargs):
        super(MDSRTGO_scr_3, self).__init__(**kwargs)
        # assigning function and class to variable
        layout_mds = MDSRTGO_layout()
        layout = MDFloatLayout()
        img = get_images()

        # assigning class to variable
        btn_back_to_main = MDIconButton(
            on_press=self.screen_switch,
            font_size='45sp',
            pos_hint={'center_x':0.07, 'center_y':0.96},
            icon='arrow-left',
            theme_text_color='Custom',
            text_color=[.2510,.5529,.9765,1],
            md_bg_color=[0,0,0,0]
        )

        lbl_top_name = MDLabel(
            text='APP INFORMATION',
            halign='left',
            size_hint=(None,None), size=(450,40),
            pos_hint={'center_x':0.56, 'center_y':0.96},
            font_style='H5',
            theme_text_color='Primary',
            markup=True
        )

        img_logo_mdsanima = Image(
            source=resource_path(img[3]),
            size=(211,211), pos=self.pos,
            size_hint_y=None,
            allow_stretch=True,
        )

        img_ascii_mdsanima = Image(
            source=resource_path(img[4]),
            size=(422,422), pos=self.pos,
            size_hint_y=None,
            allow_stretch=True,
        )

        # add widget layout
        layout.add_widget(btn_back_to_main)
        layout.add_widget(lbl_top_name)

        # draw info version and background
        layout_mds.img_background(img[2])
        layout_mds.lbl_info_version()
        self.add_widget(layout_mds)

        # draw all widget
        self.add_widget(layout)

        # assigning class to variable
        layout_box = MDBoxLayout(padding=[0,60,0,35], orientation='vertical')
        scroll_view = ScrollView()
        self.list_view = MDList()

        # add widget layout
        layout_box.add_widget(scroll_view)
        scroll_view.add_widget(self.list_view)

        # assigning function to variable brake labels
        break_info = self.lbl_info_break

        # add widget layout
        self.lbl_info_top('MDSANIMA RT GO APP')
        self.lbl_info_bottom('Created by Marcin Różewski')
        break_info()
        self.lbl_info_top('GIVE ME A FEEDBACK')
        self.lbl_info_bottom('admin@app.mdsanima.com')
        break_info()
        self.lbl_info_top('DEVELOPMENT')
        self.lbl_info_bottom('We developing these application for you!')
        self.lbl_info_bottom('1.5K lines of code it written by MDSANIMA')
        break_info()
        self.list_view.add_widget(img_logo_mdsanima)
        break_info()
        self.lbl_info_top('APP INFORMATION')
        self.lbl_info_app('app name', 'MDSANIMA RT GO')
        self.lbl_info_app('license', 'Apache - 2.0')
        self.lbl_info_app('source code on', 'GitHub')
        self.lbl_info_app('release version', 'v' + __version__)
        self.lbl_info_app('release on', 'August 19, 2021')
        self.lbl_info_app('language', 'Python v3.8.6 64-bit')
        self.lbl_info_app('framework', 'Kivy v2.0.0')
        self.lbl_info_app(' ', 'KivyMD v0.104.2')
        self.lbl_info_app('cloud provider', 'Google Cloud Platform', 'Hint')
        self.lbl_info_app(' ', 'Firebase Realtime Database', 'Hint')
        self.lbl_info_app(' ', 'Firebase Storage', 'Hint')
        self.lbl_info_app('distribution', 'Cross Platform')
        self.lbl_info_app(' ', 'Microsoft Windows 10')
        self.lbl_info_app(' ', 'Linux Ubuntu 20.04')
        self.lbl_info_app(' ', 'Android API 21 - 29')
        self.lbl_info_app(' ', 'macOSX - Coming Soon', 'Hint')
        self.lbl_info_app(' ', 'iOS - Coming Soon', 'Hint')
        break_info()

        # initial variable info text
        info_vfx_studio = (
            "Let me introduce myself. I'm in charge of head of VFX and Game "
            + "Development for MDSANIMA. We've been working on VFX and Game "
            + "Development for the past 10 years now."
            + "\n\n"
            + "We love Houdini Sidefx so much. We create visual effect like "
            + "smoke, water, cloth simulation, procedural 3D modeling and "
            + "much more we do with these software. If you want to, you can "
            + "make digital asset for Unreal Engine 4 tweak parameter of your "
            + "asset directly in game engine. In this way, you can make "
            + "perfect game with only this two excellent software."
            + "\n\n"
            + "Of course we love Blender too. In these software, we make "
            + "3D models, sculpt and render. Also we have experienced on "
            + "Substance Painter UDIM workflow, Zbrush, Coat 3D, Nuke, Black "
            + "Magic Davinci Resolve, Black Magic Fusion and many many more "
            + "great software to do making games, cinematic, commercial, as "
            + "well as app development."
            + "\n\n"
            + "We recently discovered a great software to do rendering and "
            + "layout 3d stuff called Clarisse iFX. This software can handle "
            + "off the limit the biggest 3D scenes ever, without any display "
            + "problems. Handle over 10 trylion polygon and no more lagging "
            + "on 3D viewport, no more LOD - level of detail."
        )

        info_app_devs = (
            "Our studio also experienced in App Development. We're "
            + "programming in Python, VEX, C#, Java, PHP, HTML and SQL. "
            + "Development Framework Xamarin, Kivy, KivyMD, PySide2, PyQt5 "
            + "and more. Our favorite programing software is Visual Studio "
            + "Code work with GIT."
            + "\n\n"
            + "We'r expanded our experience in Cloud Computing like Linux "
            + "Ubuntu Spot Instance in AWS, S3, Microsoft Azure, Oracle, "
            + "Google Cloud Platform with Realtime Database in Firebase."
            + "\n\n"
            + "We really like command line rendering, so much fun!"
        )

        # add widget layout
        self.lbl_info_top('MDSANIMA VFX Studio')
        self.lbl_info_mdsanima(info_vfx_studio, 'justify', '520sp')
        break_info()
        self.lbl_info_top('APP DEVS')
        self.lbl_info_mdsanima(info_app_devs, 'justify', '255sp')
        break_info()
        self.lbl_info_top('OUR CLIENTS')
        self.lbl_info_bottom('admin@app.mdsanima.com')
        break_info()
        self.list_view.add_widget(img_ascii_mdsanima)

        # draw all widget
        self.add_widget(layout_box)

    def screen_switch(self, instance):
        self.manager.current = 'scr_2'
        self.manager.transition.direction = 'right'

    def lbl_info_top(self, text_info: str):
        info_top = MDLabel(
            text=text_info,
            halign='center',
            height='15sp',
            #font_style='H6',
            size_hint_y=None,
            theme_text_color='Custom',
            text_color=[.2510,.5529,.9765,1]
        )
        self.list_view.add_widget(info_top)

    def lbl_info_bottom(self, text_info: str, height: str='30sp'):
        info_bottom = MDLabel(
            text=text_info,
            halign='center',
            height=height,
            size_hint_y=None,
            theme_text_color='Secondary'
        )
        self.list_view.add_widget(info_bottom)

    def lbl_info_break(self):
        info_break = MDLabel(text=' ', height='30sp', size_hint_y=None)
        self.list_view.add_widget(info_break)

    def lbl_info_app(self, l_text: str, r_text: str, r_color: str='Secondary'):
        layout_box = MDBoxLayout(
            orientation='horizontal',
            size_hint_x=None, size_hint_y=None,
            width='450sp', height='30sp'
        )
        lbl_left = MDLabel(
            text=l_text,
            halign='right',
            size_hint_x=None, size_hint_y=None,
            width='200sp', height='30sp',
            theme_text_color='Hint'
        )
        lbl_middle = MDLabel(
            text=' ',
            halign = 'center',
            size_hint_x=None, size_hint_y=None,
            width='10sp', height='30sp'
        )
        lbl_right = MDLabel(
            text=r_text,
            size_hint_y=None,
            height='30sp',
            theme_text_color=r_color
        )
        layout_box.add_widget(lbl_left)
        layout_box.add_widget(lbl_middle)
        layout_box.add_widget(lbl_right)
        self.list_view.add_widget(layout_box)

    def lbl_info_mdsanima(self, text_info: str, halign: str, height: str):
        info_mdsanima = MDLabel(
            text=text_info,
            halign=halign,
            width='512sp', height=height,
            padding_x=40, line_height=1.2,
            size_hint_x=None, size_hint_y=None,
            theme_text_color='Secondary'
        )
        self.list_view.add_widget(info_mdsanima)


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
