import time
import os
from datetime import datetime

def wait_for_next_five_minute_mark():
    while True:
        now = datetime.now()
        seconds_until_next_chime = (5 - now.minute % 5) * 60 - now.second
        time.sleep(seconds_until_next_chime)
        print(f"Chime! 🛎️ {datetime.now().strftime('%H:%M:%S')}")
        os.system("afplay /System/Library/Sounds/Glass.aiff")

try:
    wait_for_next_five_minute_mark()
except KeyboardInterrupt:
    print("\nChime program stopped.")
