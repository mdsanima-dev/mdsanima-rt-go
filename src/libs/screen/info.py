"""
Calculation module. Here is a main screen render time calculation.
"""


from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.list import MDList

from __init__ import __version__, resource_path
from config.image import get_images
from libs.screen.layout import MDSRTGO_layout


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
        self.lbl_info_app('first release on', 'August 19, 2021')
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

