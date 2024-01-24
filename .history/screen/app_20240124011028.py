# pylint: disable=no-member

import cv2
from colorama import Style
from multiprocessing import Pool, cpu_count

def process_row(pixel):
    color_codes = ""
    for value in pixel:
        color_code = f"\033[48;2;{value[0]};{value[1]};{value[2]}m"
        reset_color = Style.RESET_ALL
        color_codes += f"{color_code}⠀{reset_color}"
    return color_codes + "\n"

def process_frame(frame):
    pixels = frame
    with Pool(cpu_count()) as pool:
        color_codes_rows = pool.map(process_row, pixels)
    return ''.join(color_codes_rows)

video_path = r"cat.mp4"
cap = cv2.VideoCapture(video_path)

while True:
    start_time = time.time()

    ret, frame = cap.read()
    if not ret:
        break

    text = process_frame(frame)
    print(text)

    elapsed_time = time.time() - start_time
    time.sleep(max(0, 1 - elapsed_time))
