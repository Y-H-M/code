# pylint: skip-file

import cv2
from PIL
cap = cv2.VideoCapture('cat.mp4')
ret, frame = cap.read()
print(frame)
while True:
    ret, frame = cap.read()
    