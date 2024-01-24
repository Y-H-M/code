import imageio
from colorama import Fore, Style

def print_video_with_highlight(file_path):
    video_reader = imageio.get_reader(file_path)

    for frame_number, frame in enumerate(video_reader):
        print(f"{Fore.GREEN}Frame {frame_number + 1}{Style.RESET_ALL}")
        for row in frame:
            for pixel in row:
                # You can customize the highlighting based on pixel values or other conditions
                if pixel[0] > 200 and pixel[1] > 200 and pixel[2] > 200:
                    print(f"{Fore.RED}█{Style.RESET_ALL}", end="")
                else:
                    print("█", end="")
            print()

        input("Press Enter for the next frame...")

if __name__ == "__main__":
    video_path = "cat.mp4"
    print_video_with_highlight(video_path)
