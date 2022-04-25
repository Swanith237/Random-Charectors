import random
import time
import sys
from charectors import char
import pyautogui

print("Starting...")
time.sleep(1)

print("Charectors: \n", char)
print()

while True:
    randomized_symbol = random.choice(char)
    time.sleep(0.1)
    print(randomized_symbol)

    pos = pyautogui.position()
    #print(pos)
    if pos == ("Point(x=0, y=0)"):
        sys.exit()
    else:
        pass