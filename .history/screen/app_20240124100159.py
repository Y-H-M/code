# pylint: skip-file

import cv2
from PIL import Image

cap = cv2.VideoCapture('cat.mp4')
while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    