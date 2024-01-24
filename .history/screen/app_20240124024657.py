import cv2
import numpy as np

def process_frame(frame):
    height, width, _ = frame.shape
    color_codes_rows = []

    for row in range(height):
        colored_row = ""
        for col in range(width):
            pixel = frame[row, col, :]
            colored_block = f"\033[48;5;{closest_ansi_color(pixel)}m{'█'}\033[0m"
            colored_row += colored_block
        color_codes_rows.append(colored_row)

    return color_codes_rows

def closest_ansi_color(rgb):
    # This is a basic example, you may need a more sophisticated approach
    # to map RGB values to ANSI color codes
    # Here, we use a simple Euclidean distance to find the closest ANSI color
    color_palette = [
        0, 1, 2, 4, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24,
        25, 27, 28, 29, 31, 32, 33, 34, 35, 36, 37, 39, 40, 41, 42, 43, 44, 45, 47,
        49, 50, 51, 52, 53, 54, 55, 57, 58, 59, 60, 61, 63, 65, 66, 67, 68, 69, 71,
        72, 73, 74, 75, 76, 77, 79, 80, 81, 82, 83, 84, 85, 87, 88, 89, 90, 91, 92,
        93, 95, 97, 98, 99, 100, 101, 103, 104, 105, 106, 107, 108, 109, 111, 112,
        113, 114, 115, 116, 117, 119, 121, 122, 123, 124, 125, 127, 128, 129, 130,
        131, 132, 133, 135, 137, 138, 139, 140, 141, 143, 144, 145, 146, 147, 148,
        149, 151, 153, 154, 155, 156, 157, 159, 161, 162, 163, 164, 165, 167, 168,
        169, 170, 171, 172, 173, 175, 177, 178, 179, 180, 181, 183, 184, 185, 186,
        187, 188, 189, 191, 193, 194, 195, 196, 197, 199, 200, 201, 202, 203, 204,
        205, 207, 209, 210, 211, 212, 213, 215, 216, 217, 218, 219, 220, 221, 223,
        224, 225, 226, 227, 228, 229, 231, 233, 234, 235, 236, 237, 239, 240, 241,
        242, 243, 244, 245, 247, 249, 250, 251, 252, 253, 255
    ]
    closest_color = min(color_palette, key=lambda x: np.linalg.norm(np.array(rgb) - np.array(color_to_rgb(x))))
    return closest_color

def color_to_rgb(color):
    # Convert ANSI color code to RGB
    r = (color >> 16) & 0xFF
    g = (color >> 8) & 0xFF
    b = color & 0xFF
    return r, g, b

# Load the video
cap = cv2.VideoCapture('cat.mp4')

# Read the first frame
ret, first_frame = cap.read()

if ret:
    # Process the first frame
    text = process_frame(first_frame)

    # Print the processed frame
    for row in text:
        print(row, end='')
else:
    print("Failed to read the first frame from the video.")

# Release the video capture object
cap.release()
