def program():
    import random
    import time
    import os
    import sys
    import pyautogui
    import colorama
    from colorama import Style
    from charectors import char

    colorama.init()
    print("This program is going to be continously Printing Random Charectors into the Terminal.")

    clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

    def confirmation():
        confirm = input("Are you Sure you Want to Continue? (y/n): ")

        if confirm == "y":
            print()
            print("Okay, Starting...")
            print()
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

        elif confirm == "n":
            print()
            print("Okay, Bye!")
            time.sleep(2)

            print(f"{Style.BRIGHT}Made by: Swanith")
            time.sleep(0.5)
            print(f"{Style.BRIGHT}Discord: FightKnight#6129")
            print(f"{Style.BRIGHT}Github: Swanith237 - https://github.com/Swanith237/")

            time.sleep(10)
            clearConsole()

            sys.exit()

        else:
            print()
            print("Please enter 'y' or 'n'!")
            confirmation()

    confirmation()
program()