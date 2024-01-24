import time

start_time = time.time()

while True:
    # Calculate time elapsed
    elapsed_time = time.time() - start_time

    # Update and print the text with time elapsed
    text = f"Hello, World! Time Elapsed: {elapsed_time:.2f} seconds"
    print(text, end='\r')

    # Wait for 1 second
    time.sleep(1)
