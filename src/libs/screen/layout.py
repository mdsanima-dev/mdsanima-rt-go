"""
Layout module. Here is a render time calculation function.
"""


from __init__ import __version__

from datetime import datetime, timedelta

from humanfriendly import format_timespan
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDIconButton
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.progressbar import MDProgressBar
from kivymd.uix.slider import MDSlider
from kivymd.uix.textfield import MDTextField

from libs.timecode import frames_to_time_code


class MDSRTGO_layout(Screen):
    """
    Class method for `label` or other function when used multiple times.
    """
    def __init__(self, **kwargs):
        super(MDSRTGO_layout, self).__init__(**kwargs)
        self.hours = 0
        self.minutes = 0
        self.seconds = 0
        self.frames = 240
        self.total_render_time = '0:00:00'

    def lbl_top(self, icon: str, ic_on_press: None, lbl_text: str):
        """
        Top navigation text and icons.

        :param icon: icon name
        :type icon: str
        :param ic_on_press: function to switch screen or other features
        :type ic_on_press: None
        :param lbl_text: label text on the top nawigation
        :type lbl_text: str
        """
        layout = MDBoxLayout()
        layout.orientation = 'horizontal'
        layout.padding = ['10sp', '10sp', 0, 0]

        icons = MDIconButton()
        icons.icon = icon
        icons.size_hint_x = None
        icons.size_hint_y = None
        icons.pos_hint = {'top': 1}
        icons.theme_text_color = 'Custom'
        icons.text_color = [0.2510, 0.5529, 0.9765, 1]
        icons.on_press = ic_on_press

        label = MDLabel()
        label.text = lbl_text
        label.width = '550sp'
        label.height = icons.size[0]
        label.size_hint_x = None
        label.size_hint_y = None
        label.pos_hint = {'top': 1}
        label.font_style = 'H5'
        label.theme_text_color = 'Primary'
        label.markup = True

        layout.add_widget(icons)
        layout.add_widget(label)
        self.add_widget(layout)

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
            source=image,
            size=self.size, pos=self.pos,
            width='1075sp', height='1849sp',
            size_hint_x=None, size_hint_y=None,
            pos_hint={'center_x':0.5, 'center_y':0.5},
            allow_stretch=True
        )
        layout.add_widget(background)
        self.add_widget(layout)

    def tfl_number_of_frames(self, pos: float):
        layout = MDFloatLayout()
        self.number_of_frames = MDTextField(
            required=True, text=str(self.frames),
            helper_text_mode='on_error',
            input_filter='int', max_text_length=6,
            size_hint=(0.9,None),
            pos_hint={'center_x':0.5, 'top':pos},
            current_hint_text_color=[.957,.573,.020,1],
            font_size='26sp'
        )
        self.number_of_frames.bind(text=self.on_fields_frames)
        self.number_of_frames.bind(text=self.on_slider_result)
        layout.add_widget(self.number_of_frames)
        self.add_widget(layout)

    def lbl_text(
            self, text: str, pos: int, style: str,
            color: str, halign: str='left'
    ):
        layout = MDFloatLayout()
        text_rt_one_result = MDLabel(
            text=text,
            halign=halign,
            size_hint=(0.9,None), size=('200sp','40sp'),
            pos_hint={'center_x':0.5, 'top':pos},
            font_style=style,
            theme_text_color=color
        )
        layout.add_widget(text_rt_one_result)
        self.add_widget(layout)

    def lbl_statistic(self, text: str, pos: int, style: str, color: str):
        layout = MDFloatLayout()
        self.text_statistic = MDLabel(
            text=text,
            halign='right',
            size_hint=(0.9,None), size=('200sp','40sp'),
            pos_hint={'center_x':0.5, 'top':pos},
            font_style=style,
            theme_text_color=color
        )
        layout.add_widget(self.text_statistic)
        self.add_widget(layout)

    def lbl_time_code(self, text: str, pos: int, style: str, color: str):
        layout = MDFloatLayout()
        self.text_time_code = MDLabel(
            text=text,
            halign='right',
            size_hint=(0.9,None), size=('200sp','40sp'),
            pos_hint={'center_x':0.5, 'top':pos},
            font_style=style,
            theme_text_color=color,
            text_color=[.957,.573,.020,1],
        )
        layout.add_widget(self.text_time_code)
        self.add_widget(layout)

    def lbl_time_code_human(self, text: str, pos: int, style: str, color: str):
        layout = MDFloatLayout()
        self.time_code_human = MDLabel(
            text=text,
            halign='right',
            size_hint=(0.9,None), size=('200sp','40sp'),
            pos_hint={'center_x':0.5, 'top':pos},
            font_style=style,
            theme_text_color=color
        )
        layout.add_widget(self.time_code_human)
        self.add_widget(layout)

    def lbl_rt_result_one(self, text: str, pos: int, style: str, color: str):
        layout = MDFloatLayout()
        self.text_rt_one_result = MDLabel(
            text=text,
            halign='right',
            size_hint=(0.9,None), size=('200sp','40sp'),
            pos_hint={'center_x':0.5, 'top':pos},
            font_style=style,
            theme_text_color=color
        )
        layout.add_widget(self.text_rt_one_result)
        self.add_widget(layout)

    def lbl_rt_result_human(self, text: str, pos: int, style: str, color: str):
        layout = MDFloatLayout()
        self.hum_rt_one_result = MDLabel(
            text=text,
            halign='right',
            size_hint=(0.9,None), size=('200sp','40sp'),
            pos_hint={'center_x':0.5, 'top':pos},
            font_style=style,
            theme_text_color=color
        )
        layout.add_widget(self.hum_rt_one_result)
        self.add_widget(layout)

    def sld_slider(self):
        layout = MDFloatLayout()
        slider_hours = MDSlider(
            min=0, max=23, value=0,
            size_hint=(0.94,None), size=('200sp','40sp'),
            pos_hint={'center_x':0.5, 'top':0.80},
            color='#7c7c7c',
            show_off=False,
            hint_text_color=[.2510,.5529,.9765,0]
        )
        slider_minutes = MDSlider(
            min=0, max=59, value=0,
            size_hint=(0.94,None), size=('200sp','40sp'),
            pos_hint={'center_x':0.5, 'top':0.72},
            color='#7c7c7c',
            show_off=False,
            hint_text_color=[.2510,.5529,.9765,0]
        )
        slider_seconds = MDSlider(
            min=0, max=59, value=0,
            size_hint=(0.94,None), size=('200sp','40sp'),
            pos_hint={'center_x':0.5, 'top':0.64},
            color='#7c7c7c',
            show_off=False,
            hint_text_color=[.2510,.5529,.9765,0]
        )
        slider_hours.bind(value=self.on_slider_hours)
        slider_minutes.bind(value=self.on_slider_minutes)
        slider_seconds.bind(value=self.on_slider_seconds)
        slider_hours.bind(value=self.on_slider_result)
        slider_minutes.bind(value=self.on_slider_result)
        slider_seconds.bind(value=self.on_slider_result)
        layout.add_widget(slider_hours)
        layout.add_widget(slider_minutes)
        layout.add_widget(slider_seconds)
        self.add_widget(layout)

    def lbl_rt_total(
            self, text: str, pos: int, style: str,
            color: str, halign: str='center'
    ):
        layout = MDFloatLayout()
        self.render_time_total = MDLabel(
            text=text,
            halign=halign,
            size_hint=(0.9,None), size=('200sp','40sp'),
            pos_hint={'center_x':0.5, 'top':pos},
            font_style=style,
            theme_text_color=color,
            text_color=[.2510,.5529,.9765,1]
        )
        self.render_time_total_human = MDLabel(
            text='0 SECONDS',
            halign=halign,
            size_hint=(0.9,None), size=('200sp','40sp'),
            pos_hint={'center_x':0.5, 'top':pos - 0.025},
            font_style='Overline',
            theme_text_color='Hint',
            text_color=[.2510,.5529,.9765,1]
        )
        layout.add_widget(self.render_time_total)
        layout.add_widget(self.render_time_total_human)
        self.add_widget(layout)

    def lbl_rt_date_start(
            self, text: str, pos: int, style: str,
            color: str, halign: str='center'
    ):
        layout = MDFloatLayout()
        self.render_time_date_start = MDLabel(
            text=text,
            halign=halign,
            size_hint=(0.9,None), size=('200sp','40sp'),
            pos_hint={'center_x':0.5, 'top':pos},
            font_style=style,
            theme_text_color=color,
            text_color=[.957,.573,.02,1]
        )
        layout.add_widget(self.render_time_date_start)
        self.add_widget(layout)

    def lbl_rt_date_complete(
            self, text: str, pos: int, style: str,
            color: str, halign: str='center'
    ):
        layout = MDFloatLayout()
        self.render_time_date_complete = MDLabel(
            text=text,
            halign=halign,
            size_hint=(0.9,None), size=('200sp','40sp'),
            pos_hint={'center_x':0.5, 'top':pos},
            font_style=style,
            theme_text_color=color,
            text_color=[.2510,.5529,.9765,1]
        )
        layout.add_widget(self.render_time_date_complete)
        self.add_widget(layout)

    def pgb_progress(self):
        layout = MDFloatLayout()
        self.progress_rt = MDProgressBar(
            type='determinate',
            size_hint=(1,None),
            pos_hint={'center_x':0.5, 'center_y':0.005},
            running_duration=0.4,
            catching_duration=0.8,
            color=[1,.0,.0,1]
        )
        layout.add_widget(self.progress_rt)
        self.progress_rt.start()
        self.add_widget(layout)

    def on_slider_hours(self, instance, slider_value):
        self.hours = '%d' % slider_value

    def on_slider_minutes(self, instance, slider_value):
        self.minutes = '%d' % slider_value

    def on_slider_seconds(self, instance, slider_value):
        self.seconds = '%d' % slider_value

    def on_slider_result(self, instance, slider_value):
        hours = int(self.hours) if int(self.hours) <= 23 else 0
        minutes = int(self.minutes) if int(self.minutes) <= 59 else 0
        seconds = int(self.seconds) if int(self.seconds) <= 59 else 0
        delta_hours = timedelta(hours=int(hours))
        delta_minutes = timedelta(minutes=int(minutes))
        delta_seconds = timedelta(seconds=int(seconds))
        delta_rt_one_frame = delta_hours + delta_minutes + delta_seconds
        self.total_render_time = delta_rt_one_frame * self.frames
        self.text_rt_one_result.text = str(delta_rt_one_frame)
        self.hum_rt_one_result.text = str(format_timespan(delta_rt_one_frame))
        self.render_time_total.text = str(self.total_render_time).upper()
        self.render_time_total_human.text = str(
            format_timespan(self.total_render_time)
        )
        if hours or minutes or seconds >= 1:
            self.text_rt_one_result.theme_text_color = 'Custom'
            self.text_rt_one_result.text_color = [.2510,.5529,.9765,1]
            self.progress_rt.stop()
        else:
            self.text_rt_one_result.theme_text_color = 'Error'
            self.progress_rt.start()
        now = datetime.now()
        date_now = str(now.strftime('%H:%M:%S  %Y-%m-%d  %A')).upper()
        self.render_time_date_start.text = str(date_now)
        sec_complet = timedelta(seconds=self.total_render_time.total_seconds())
        complete = now + sec_complet
        date_complet = str(complete.strftime('%H:%M:%S  %Y-%m-%d  %A')).upper()
        self.render_time_date_complete.text = str(date_complet)

    def on_fields_frames(self, instance, frames_value):
        frames = 0 if frames_value == '' else frames_value
        frames_tc = frames_to_time_code(int(frames), 24)
        self.frames = int(frames)
        self.text_time_code.text = frames_tc
        hours = str(frames_tc)[:2]
        minut = str(frames_tc)[3:5]
        secnd = str(frames_tc)[6:8]
        frame = str(frames_tc)[9:]
        frame_int = int(frame)
        fra_chk = ' FRAME' if frame_int == 1 else ' FRAMES'
        frames_end = '' if frame_int == 0 else ', ' + str(frame_int) + fra_chk
        delta_time_code = timedelta(
            hours=int(hours), minutes=int(minut), seconds=int(secnd)
        )
        self.time_code_human.text = str(
            format_timespan(delta_time_code)) + str(frames_end
        )
