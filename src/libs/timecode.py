
def frames_to_time_code(frames: int, fps: int) -> str:
    """
    Function converts frames to time code `00:00:00:00` format

    :param frames: number of total frames
    :type frames: int
    :param fps: frames per second
    :type fps: int
    :return: time code format
    :rtype: str
    """
    sec_in_min = 60
    fra_in_min = sec_in_min * fps
    fra_in_hrs = sec_in_min * fra_in_min

    hrs = int(frames / fra_in_hrs)
    min = int(frames / fra_in_min) % sec_in_min
    sec = int((frames % fra_in_min) / fps)
    fra = int((frames % fra_in_min) % fps)

    time_code = str("%02d:%02d:%02d:%02d" % (hrs, min, sec, fra))

    return time_code
