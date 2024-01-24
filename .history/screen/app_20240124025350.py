import cv2

def print_video_with_highlight(file_path, width=80):
    cap = cv2.VideoCapture(file_path)

    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            break

        print("Press 'q' to quit.")
        cv2.imshow('Video', frame)

        # Resize the frame for better display
        resized_frame = cv2.resize(frame, (width, width // 2))

        for y in range(resized_frame.shape[0]):
            for x in range(resized_frame.shape[1]):
                pixel = resized_frame[y, x]
                # You can customize the highlighting based on pixel values or other conditions
                if all(value > 200 for value in pixel):
                    print('\033[91m\033[107m#', end="")
                else:
                    print(" ", end="")
            print('\033[0m')  # Reset color after each row

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    video_path = "cat.mp4"
    print_video_with_highlight(video_path)
