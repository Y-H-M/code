# pylint: skip-file

import cv2
from PIL import Image

def

cap = cv2.VideoCapture('cat.mp4')
while True:
    ret, frame = cap.read()
    if not ret:
        break
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(rgb)
    for i in range(img.size[1]):
        for j in range(img.size[0]):
            output_text()
    
    