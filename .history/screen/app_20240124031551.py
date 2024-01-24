import cv2
from PIL import Image

# Open the video file using cv2
video_capture = cv2.VideoCapture('cat.mp4')

# Check if the video file opened successfully
if not video_capture.isOpened():
    print("Error: Could not open video file.")
    exit()

while True:
    # Read a frame
    success, frame = video_capture.read()

    # Break the loop if the video has ended
    if not success:
        print("End of video.")
        break

    # Convert the OpenCV BGR image to RGB
    rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Convert the image array to a PIL Image
    pil_image = Image.fromarray(rgb_image)
    
    # Print the frame
    text = ""
    for row in range(pil_image.size[1]-1):
        for height in range(pil_image.size[0]-1):
            background_color = pil_image.getpixel((row, height))
            print(f"\033[48;2;{background_color[0]};{background_color[1]};{background_color[2]}m O \033[0m")
        text += "\n"
    print(text)

