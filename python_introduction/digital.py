import time
import os

def digital_clock():
    try:
        while True:
            # Get current time
            current_time = time.strftime("%H:%M:%S")
            
            # Clear the terminal (works on Windows and Linux/macOS)
            os.system('cls' if os.name == 'nt' else 'clear')
            
            # Print time with a cool blinking effect
            print(f"\033[1;32m⏰  {current_time}  ⏰\033[0m")  # Green bold text
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nClock stopped. Have a great day! ⏱️")

digital_clock()
