import time

while True:
    # Update and print the text
    text = "Hello, World!"
    print(text, end='\r')  # \r is used to overwrite the previous line

    # Wait for 1 second
    time.sleep(1)
