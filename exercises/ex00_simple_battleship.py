"""EX01 - Simple Battleship - A cute step toward Battles"""

__author__ = "730544769"

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"
guess_result: str = ""
storage: str = ""

shot1: str = input("Pick a secret boat location between 1 and 4: ")
shot1 = int(shot1)
if shot1 < 1:
    print(f"Error! {shot1} too low! ")
    exit()
if shot1 > 4:
    print(f"Error! {shot1} too high! ")
    exit()

guess1: str = input("Guess a number between 1 and 4: ")
guess1 = int(guess1)
if guess1 < 1:
    print(f"Error! {guess1} too low! ")
    exit()
if guess1 > 4:
    print(f"Error! {guess1} too high! ")
    exit()
if shot1 == guess1:
    guess_result = RED_BOX
    if shot1 == 1:
        storage = f"{guess_result}{BLUE_BOX}{BLUE_BOX}{BLUE_BOX}"
        print(f"{storage}")
    if shot1 == 2:
        storage = f"{BLUE_BOX}{guess_result}{BLUE_BOX}{BLUE_BOX}"
        print(f"{storage}")
    if shot1 == 3: 
        storage = f"{BLUE_BOX}{BLUE_BOX}{guess_result}{BLUE_BOX}"
        print("Correct! You hit the ship. ")
    if shot1 == 4:
        storage = f"{BLUE_BOX}{BLUE_BOX}{BLUE_BOX}{guess_result}"
        print(f"{storage}")
else:
    guess_result = WHITE_BOX
    if shot1 == 1:
        storage = f"{guess_result}{BLUE_BOX}{BLUE_BOX}{BLUE_BOX}"
        print(f"{storage}")
    if shot1 == 2:
        storage = f"{BLUE_BOX}{guess_result}{BLUE_BOX}{BLUE_BOX}"
        print(f"{storage}")
    if shot1 == 3: 
        storage = f"{BLUE_BOX}{BLUE_BOX}{guess_result}{BLUE_BOX}"
        print("Correct! You hit the ship. ")
    if shot1 == 4:
        storage = f"{BLUE_BOX}{BLUE_BOX}{BLUE_BOX}{guess_result}"
        print(f"{storage}")
        print("Incorrect! You missed the ship. ")
