# pylint: skip-file

import cv2
from PIL import Image

def output_text(rgb):
    text = f"\033[48;2;{rgb[0]};{rgb[1]};{rgb[2]}mO\033[0m]"
    return text

cap = cv2.VideoCapture('cat.mp4')
while True:
    ret, frame = cap.read()
    if not ret:
        break
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(rgb)
    text = ""
    for i in range(img.size[0] - 1):
        for j in range(img.size[1] - 1):
            text += output_text(img.getpixel((i,j)))
        text += "\n"
    print(text)
    
    