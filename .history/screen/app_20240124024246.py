# pylint: disable=no-member

import time
from multiprocessing import Pool, cpu_count
import cv2
import sys
from colorama import Style, Fore, Back

def process_row(pixel):
    colored_row = ""
    for value in pixel:
        rgb = (value[0], value[1], value[2])
        colored_block = f"{Fore.BLACK}{Back.LIGHT}{rgb}{Style.RESET_ALL}{'█'}"
        colored_row += colored_block
    return colored_row + "\n"

def process_frame(frame):
    pixels = frame
    with Pool(cpu_count()) as pool:
        color_codes_rows = pool.map(process_row, pixels)
    return ''.join(color_codes_rows)

video_path = r"cat.mp4"
cap = cv2.VideoCapture(video_path)
    
    # Save the current text for the next iteration
prev_text = ""
while True:
    start_time = time.time()

    ret, frame = cap.read()
    if not ret:
        break

    text = process_frame(frame)
    
    # Use ANSI escape codes to clear the line and move the cursor to the beginning
    sys.stdout.write("\033[F\033[K")
    sys.stdout.write(text)
    sys.stdout.flush()

    elapsed_time = time.time() - start_time
    time.sleep(max(0, 1 - elapsed_time))