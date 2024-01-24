# pylint: skip-file

import cv2
cap = cv2.VideoCapture('cat.mp4')
ret, frame = cap.read()
while true:
    cv2