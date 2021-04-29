# The most simplest timer from https://realpython.com/python-timer/#your-first-python-timer

import time

start = time.perf_counter()
# Add code to profile here

end = time.perf_counter()

print(f"Ran in: {end - start:0.4f} seconds")
