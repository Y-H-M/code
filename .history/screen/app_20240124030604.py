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

    # Display or further process the PIL image as needed
    pil_image.show()

    # You can add a delay here if you want to control the speed of the display
    # For example, you can use cv2.waitKey(30) to wait for 30 milliseconds

# Close the video capture object
video_capture.release()