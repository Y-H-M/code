import cv2
import os

def is_black_strip(frame, threshold=10):
    return cv2.mean(frame)[0] < threshold

def process_webm(input_path, output_path):
    cap = cv2.VideoCapture(input_path)

    fps = int(cap.get(cv2.CAP_PROP_FPS))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    fourcc = cv2.VideoWriter_fourcc(*'VP80')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        if not is_black_strip(frame):
            out.write(frame)

    cap.release()
    out.release()

if __name__ == "__main__":
    input_file = "i.webm"
    output_file = "o.webm"
    
    process_webm(input_file, output_file)

    # Optionally, you can remove the original input file
    # after processing to rename it to "i.webm"
    os.remove(input_file)
