import numpy as np
from colorama import Fore, Back, Style, init
from tqdm import tqdm

init()  # Initialize colorama

def process_row(pixel):
    colored_row = ""
    for value in pixel:
        rgb = tuple(value)
        ansi_color = closest_ansi_color(rgb)
        colored_block = f"{Fore.BLACK}{ansi_color}{'█'}{Style.RESET_ALL}"
        colored_row += colored_block
    return colored_row + "\n"

def closest_ansi_color(rgb):
    # This is a basic example, you may need a more sophisticated approach
    # to map RGB values to ANSI color codes
    # Here, we use a simple Euclidean distance to find the closest ANSI color
    color_palette = [
        (0, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255),  # Black, Red, Green, Blue
        # Add more ANSI color codes as needed
    ]
    closest_color = min(color_palette, key=lambda x: np.linalg.norm(np.array(rgb) - np.array(x)))
    return Back.rgb(*closest_color)

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
