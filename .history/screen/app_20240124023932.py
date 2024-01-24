# pylint: disable=no-member

import time
from multiprocessing import Pool, cpu_count
import cv2
import sys
from colorama import Style

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

prev_text = ""

while True:
    start_time = time.time()

    ret, frame = cap.read()
    if not ret:
        break

    text = process_frame(frame)
    
    # Calculate the number of spaces needed to clear the line
    num_spaces = max(len(text), len(prev_text))
    
    # Use carriage return and print spaces to clear the line
    sys.stdout.write('\r' + ' ' * num_spaces)
    sys.stdout.write('\r' + text)
    sys.stdout.flush()

    elapsed_time = time.time() - start_time
    time.sleep(max(0, 1 - elapsed_time))
    
    # Save the current text for the next iteration
    prev_text = text
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