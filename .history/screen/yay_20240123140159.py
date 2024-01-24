import time
import pygame
from pygame.locals import QUIT

def update_progress_bar(percentage):
    # Function to print a progress bar with the given percentage
    bar_length = 20
    filled_length = int(bar_length * percentage)
    bar = '[' + '=' * filled_length + ' ' * (bar_length - filled_length) + ']'
    print("\rProgress: {}% {}".format(int(percentage * 100), bar), end='', flush=True)

def run_timer_with_audio(duration, audio_file_path):
    # Initialize Pygame and mixer
    pygame.init()
    pygame.mixer.init()

    # Load the audio file
    pygame.mixer.music.load(audio_file_path)

    # Run a timer for the specified duration
    start_time = time.time()
    end_time = start_time + duration

    # Start playing the audio
    pygame.mixer.music.play()

    while time.time() < end_time:
        elapsed_time = time.time() - start_time
        progress_percentage = elapsed_time / duration
        update_progress_bar(progress_percentage)
        time.sleep(0.1)  # Adjust the sleep duration for smoother progress updates

    # Stop playing the audio
    pygame.mixer.music.stop()

    # Ensure the progress bar is complete at the end
    update_progress_bar(1.0)
    print("\nTimer completed!")

    # Quit Pygame
    pygame.quit()

# Replace 'your_audio_file.mp3' with the path to your audio file
audio_file_path = 'BGM.mp3'

# Run the timer with audio for 10 seconds
run_timer_with_audio(10, audio_file_path)
