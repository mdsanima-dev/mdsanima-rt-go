"""
Main application MDSANIMA-RT-GO
"""


from . import __version__

import kivy
kivy.require('2.0.0')

from kivy import Config


# set configuration windows
Config.set('graphics', 'width', '500')
Config.set('graphics', 'height', '860')
Config.set('graphics', 'minimum_width', '500')
Config.set('graphics', 'minimum_height', '600')
Config.set('graphics', 'resizable', False)

