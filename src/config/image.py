"""
Set images resources
"""


from utils.resource import resource_path


app_icon = resource_path('image/ic_launcher/res/mipmap-xhdpi/ic_launcher.png')
bg_welcome = resource_path('image/bacground/bg_1.png')
bg_main = resource_path('image/bacground/bg_2.png')
logo_web = resource_path('image/ic_launcher/web_hi_res_512.png')


def get_images():
    img_list = [app_icon, bg_welcome, bg_welcome, logo_web]
    return img_list
