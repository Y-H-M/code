import time

def update_progress_bar(percentage):
    # Function to print a progress bar with the given percentage
    bar_length = 20
    filled_length = int(bar_length * percentage)
    bar = '[' + '=' * filled_length + ' ' * (bar_length - filled_length) + ']'
    print("\rProgress: {}% {}".format(int(percentage * 100), bar), end='', flush=True)

def run_timer(duration):
    # Run a timer for the specified duration
    start_time = time.time()
    end_time = start_time + duration

    while time.time() < end_time:
        elapsed_time = time.time() - start_time
        progress_percentage = elapsed_time / duration
        update_progress_bar(progress_percentage)
        time.sleep(0.1)  # Adjust the sleep duration for smoother progress updates

    # Ensure the progress bar is complete at the end
    update_progress_bar(1.0)
    print("\nTimer completed!")

# Run the timer for 10 seconds
run_timer(10)
