def program():
    import random
    import time
    import sys
    import pyautogui
    import colorama
    from colorama import Style
    from charectors import char

    colorama.init()

    print("This program is going to be continuously printing random charectors into the terminal.")
    def conf():
        confirm = input("Are you sure you want to continue? (y/n): ")

        if confirm == "y":
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

        elif confirm == "n":
            print("Okay, Bye!")
            time.sleep(2)

            print(f"{Style.BRIGHT}Made by: Swanith")
            print(f"{Style.BRIGHT}Discord: FightKnight#6129")
            print(f"{Style.BRIGHT}Github: Swanith237")

            time.sleep(10)
            sys.exit()

    conf()
program()