import random
import time
from charectors import char

print("Starting...")
time.sleep(1)

print("Charectors: \n", char)

while True:
    randomized_symbol = random.choice(char)
    time.sleep(0.1)
    print(randomized_symbol)