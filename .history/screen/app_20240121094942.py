# pylint: disable=no-member

from PIL import Image
import cv2
from colorama import Style
import time

video_path = r"oiiai.mp4"
cap = cv2.VideoCapture(video_path)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame_rgb=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    im = Image.fromarray(frame_rgb)
    
    for j in range(im.size[1]):
        for i in range(im.size[0]):
            rgb = tuple(max(0, min(255, val)) for val in im.getpixel((i,j)))
            color_code = f"\033[48;2;{rgb[0]};{rgb[1]};{rgb[2]}m"
            reset_color = Style.RESET_ALL
            text=f"{color_code}⠀{reset_color}"
            print(text, end="")
        print()
    time.sleep(1)
    print()