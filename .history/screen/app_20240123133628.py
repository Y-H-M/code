# pylint: disable=no-member

from PIL import Image
import cv2
import numpy as np
from colorama import Style
import time

video_path = r"oiiai.mp4"
cap = cv2.VideoCapture(video_path)

while True:
    st = time.time()
    ret, frame = cap.read()
    if not ret:
        break

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    im = Image.fromarray(frame_rgb)

    pixels = np.array(im)

    text = ""
    for row in pixels:
        for rgb in row:
            rgb_clipped = np.clip(rgb, 0, 255)
            color_code = f"\033[48;2;{rgb_clipped[0]};{rgb_clipped[1]};{rgb_clipped[2]}m"
            reset_color = Style.RESET_ALL
            text += f"{color_code}⠀{reset_color}"

        text += "\n"

    print(text)
    et = time.time() - st
    time.sleep(max(0, 1 - et))
