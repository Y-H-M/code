import time

# Original print statement
print("Hello, World!", end='', flush=True)
time.sleep(2)  # Just to simulate some processing time

# Modify the content
print("\rHello, GPT-3.5!", end='', flush=True)
