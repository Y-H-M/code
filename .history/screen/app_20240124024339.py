import numpy as np
from colorama import Fore, Back, Style, init
from tqdm import tqdm

init()  # Initialize colorama

def process_row(pixel):
    colored_row = ""
    for value in pixel:
        rgb = tuple(value)
        colored_block = f"{Fore.BLACK}{Back.rgb(*rgb)}{'█'}{Style.RESET_ALL}"
        colored_row += colored_block
    return colored_row + "\n"

def process_frame(frame):
    height, width, _ = frame.shape
    color_codes_rows = []

    for row in tqdm(range(height), desc="Processing Frame"):
        color_codes_rows.append(process_row(frame[row, :, :]))

    return color_codes_rows

# Example usage
height = 10
width = 20
frame = np.random.randint(0, 256, size=(height, width, 3), dtype=np.uint8)
text = process_frame(frame)
for row in text:
    print(row, end='')
