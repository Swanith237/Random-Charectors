import random
import time

print("Starting...")
time.sleep(1)

char =["`", "~", "!", "@", "#", "$", "%", "^", "&", "*", "-", "_", "+", "=", "\\", "/", "|", ":", ";", "'", "\"", "?", ".", ",", "()", "[]", "{}", "<>", " "]
print("Charectors: \n", char)

while True:
    randomized_symbol = random.choice(char)
    time.sleep(0.1)
    print(randomized_symbol)