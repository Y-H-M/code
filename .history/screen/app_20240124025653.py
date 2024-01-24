import cv2
from PIL import Image
from colorama import Fore, Back, Style, init

# Initialize Colorama
init(autoreset=True)

# Replace 'your_video.mp4' with the path to your MP4 file
video_path = r'cat.mp4'

# Open the video file
cap = cv2.VideoCapture(video_path)

# Check if the video opened successfully
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

# Read and process frames until the end of the video
while True:
    # Read a frame from the video
    ret, frame = cap.read()

    # Break the loop if the video has ended
    if not ret:
        break

    # Convert the OpenCV frame to RGB format
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Convert the frame to a PIL Image
    pil_image = Image.fromarray(frame_rgb)

    # Convert the PIL Image to a string with Colorama highlighting
    highlighted_frame = ''
    for row in pil_image.getdata():
        for pixel in row:
            r, g, b = pixel
            # You can customize the highlighting color based on the pixel values
            if r > 128:
                highlighted_frame += Fore.RED + Back.BLACK + ' '
            else:
                highlighted_frame += Fore.GREEN + Back.BLACK + ' '
        highlighted_frame += '\n'

    # Print the highlighted frame
    print(highlighted_frame, end='')

    # Break the loop if the user presses the 'q' key
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Release the video capture object
cap.release()
