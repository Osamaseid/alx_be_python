import time
import sys
import itertools

# Rainbow colors for terminal (ANSI escape codes)
colors = [
    "\033[91m",  # Red
    "\033[93m",  # Yellow
    "\033[92m",  # Green
    "\033[96m",  # Cyan
    "\033[94m",  # Blue
    "\033[95m",  # Magenta
]

reset = "\033[0m"

def rainbow_text(text, delay=0.1):
    color_cycle = itertools.cycle(colors)
    for char in text:
        sys.stdout.write(next(color_cycle) + char + reset)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Newline at the end

# Your amazing message
message = "Welcome to Python Magic! 🌟✨"
rainbow_text(message)
