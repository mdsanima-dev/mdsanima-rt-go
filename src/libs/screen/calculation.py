"""
Calculation module. Here is a main screen render time calculation.
"""


from datetime import datetime

from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDFlatButton, MDIconButton
from kivymd.uix.floatlayout import MDFloatLayout

from __init__ import resource_path
from config.image import get_images
from libs.screen.layout import MDSRTGO_layout


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
