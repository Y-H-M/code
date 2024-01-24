# pylint: skip-file

import cv2
from PIL import Image

cap = cv2.VideoCapture('cat.mp4')
while True:
    ret, frame = cap.read()
    if not ret:
        break
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    text()
    
    