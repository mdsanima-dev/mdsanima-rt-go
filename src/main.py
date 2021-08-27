"""
Main application MDSANIMA RT GO
"""


from __init__ import __version__

import kivy
kivy.require('2.0.0')

from datetime import datetime

from __init__ import resource_path
from config.image import get_images
from config.setting import check_platform, theme_kivy
from libs.screen.layout import MDSRTGO_layout
from libs.screen.welcome import MDSRTGO_scr_1

from kivy.uix.image import Image
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.list import MDList

from plyer import notification


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
        btn_app_info = MDFlatButton()
        btn_app_info.text = 'APP INFO'
        btn_app_info.size = (101, 40)
        btn_app_info.size_hint = (None, None)
        btn_app_info.pos_hint = {'center_x': 0.5, 'y': 0.03}
        btn_app_info.on_release = self.screen_switch
        layout.add_widget(btn_app_info)

        # date time convert
        now = datetime.now()
        date_now = now.strftime('%H:%M:%S  %Y-%m-%d  %A')
        date_up = str(date_now).upper()

        # draw info version background top name
        layout_mds.img_background(resource_path(img[2]))
        rt_calc = 'RENDER TIME CALCULATOR'
        layout_mds.lbl_top('menu', self.screen_switch, rt_calc)
        layout_mds.lbl_text('NUMBER OF FRAMES', 0.94, 'Body2', 'Hint')
        layout_mds.tfl_number_of_frames(0.92)
        layout_mds.lbl_text('RENDER TIME PER FRAME', 0.85, 'Body2', 'Hint')
        layout_mds.lbl_rt_result_one('0:00:00', 0.85, 'H5', 'Error')
        layout_mds.lbl_rt_result_human('0 SECONDS', 0.83, 'Overline', 'Hint')
        layout_mds.lbl_text('HOURS', 0.82, 'Caption', 'Secondary')
        layout_mds.lbl_text('MINUTES', 0.74, 'Caption', 'Secondary')
        layout_mds.lbl_text('SECONDS', 0.66, 'Caption', 'Secondary')
        layout_mds.sld_slider()
        layout_mds.lbl_text('ANIMATION FRAME RATE', 0.59, 'Body2', 'Hint')
        layout_mds.lbl_statistic('24 FPS', 0.59, 'Body1', 'Secondary')
        layout_mds.lbl_text('DURATION TIME CODE', 0.56, 'Body2', 'Hint')
        layout_mds.lbl_time_code('00:00:10:00', 0.56, 'Body1', 'Secondary')
        layout_mds.lbl_time_code_human('10 SECONDS', 0.545, 'Overline', 'Hint')
        layout_mds.lbl_text(
            'START RENDERING', 0.50, 'Caption', 'Secondary', 'center'
        )
        layout_mds.lbl_rt_date_start(date_up, 0.48, 'Body2', 'Hint')
        layout_mds.lbl_text(
            'TOTAL RENDER TIME', 0.445, 'Subtitle1', 'Secondary', 'center'
        )
        layout_mds.lbl_rt_total('0:00:00', 0.415, 'H4', 'Error')
        layout_mds.lbl_text(
            'COMPLETE RENDERING', 0.36, 'Caption', 'Secondary', 'center'
        )
        layout_mds.lbl_rt_date_complete(date_up, 0.34, 'Body2', 'Hint')
        layout_mds.pgb_progress()
        layout_mds.lbl_info_version()
        self.add_widget(layout_mds)

        # draw all widget
        self.add_widget(layout)

    def screen_switch(self):
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
        img_logo_mdsanima = Image(
            source=resource_path(img[5]),
            size=('211sp','211sp'), pos=self.pos,
            size_hint_y=None,
            allow_stretch=True,
        )

        img_ascii_mdsanima = Image(
            source=resource_path(img[4]),
            size=('422sp','422sp'), pos=self.pos,
            size_hint_y=None,
            allow_stretch=True,
        )

        # draw info version background top name
        layout_mds.img_background(resource_path(img[2]))
        layout_mds.lbl_top('arrow-left', self.screen_switch, 'APP INFORMATION')
        layout_mds.lbl_info_version()
        self.add_widget(layout_mds)

        # draw all widget
        self.add_widget(layout)

        # assigning class to variable
        layout_box = MDBoxLayout(
            orientation='vertical',
            padding=[0,'60sp',0,'35sp']
        )
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

    def screen_switch(self):
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
