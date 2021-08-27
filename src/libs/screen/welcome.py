"""
Welcome module. Here is a first screen.
"""


from datetime import datetime

from kivy.clock import Clock
from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDFlatButton, MDIconButton
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.progressbar import MDProgressBar

from __init__ import resource_path
from config.image import get_images
from libs.screen.layout import MDSRTGO_layout


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
            font_size='35sp'
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

        pgb_progress_top = MDProgressBar(
            type='determinate', reversed=True,
            pos_hint={'center_x':0.5, 'center_y':1},
            running_duration=28,
            catching_duration=1
        )

        pgb_progress_bot = MDProgressBar(
            type='determinate',
            pos_hint={'center_x':0.5, 'center_y':0.005},
            running_duration=0.4,
            catching_duration=0.8
        )

        # add widget layout
        layout.add_widget(btn_go_rendering)
        layout.add_widget(btn_logo_mdsanima)
        layout.add_widget(lbl_click_me)

        # add progress loading animation
        pgb_progress_top.start()
        pgb_progress_bot.start()
        layout.add_widget(pgb_progress_top)
        layout.add_widget(pgb_progress_bot)

        # draw info version and background
        layout_mds.img_background(resource_path(img[1]))
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
