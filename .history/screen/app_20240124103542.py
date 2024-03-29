import cv2
from PIL import Image
import time
import sys

def output_text(rgb):
    text = f"\033[48;2;{rgb[0]};{rgb[1]};{rgb[2]}m  \033[0m"
    return text

cap = cv2.VideoCapture('cat.mp4')

while True:
    start_time = time.time()
    ret, frame = cap.read()

    print(frame.)

    if not ret:
        break

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(rgb)
    text = ""

    for i in range(img.size[1]):
        for j in range(img.size[0]):
            text += output_text(img.getpixel((j, i)))
        text += "\n"

    sys.stdout.write(text)
    sys.stdout.flush()

    elapsed_time = time.time() - start_time
    time.sleep(max(0, 5 - elapsed_time))
