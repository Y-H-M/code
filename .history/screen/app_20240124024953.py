import imageio

def print_video(file_path):
    video_reader = imageio.get_reader(file_path)

    for frame_number, frame in enumerate(video_reader):
        print(f"Frame {frame_number + 1}")
        print(frame)
        input("Press Enter for the next frame...")

if __name__ == "__main__":
    video_path = "cat.mp4"
    print_video(video_path)
