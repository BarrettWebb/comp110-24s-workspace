"""EX02 - one shot battleship. """

__author__ = "730544769"

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"
guess_results: str = ""
storage: str = ""
row_print: int = 1

secret_row: int = 4
secret_column: int = 4
boat_row = int(input("pick a row: "))
boat_row = int(boat_row)
if boat_row > 4 or boat_row < 1:
    while boat_row > 4:
        boat_row = int(input("The grid is only 4 by 4. Try again: "))
    while boat_row < 1:
        boat_row = int(input("The grid is only 4 by 4. Try again: "))
boat_column = int(input("pick a column: "))
boat_column = int(boat_column)
if boat_column > 4 or boat_row < 1:
    while boat_column > 4:
        boat_column = int(input("The grid is only 4 by 4. Try again: "))
    while boat_column < 1:
        boat_column = int(input("The grid is only 4 by 4. Try again: "))
guess_row = int(input("guess a row: "))
guess_row = int(guess_row)
if guess_row > 4 or guess_row < 1:
    while guess_row > 4:
        guess_row = int(input("The grid is only 4 by 4. Try again: "))
    while guess_row < 1:
        guess_row = int(input("The grid is only 4 by 4. Try again: "))
guess_column = int(input("guess a column: "))
guess_column = int(guess_column)
if guess_column > 4 or guess_column < 1:
    while guess_column > 4:
        guess_column = int(input("The grid is only 4 by 4. Try again: "))
    while guess_column < 1:
        guess_column = int(input("The grid is only 4 by 4. Try again: "))
if guess_row == boat_row and guess_column == boat_column:
    guess_results = RED_BOX
else:
    guess_results = WHITE_BOX

while row_print <= secret_row:
    if row_print == guess_row:
        if guess_column == 1:
            print(f"{guess_results}{BLUE_BOX}{BLUE_BOX}{BLUE_BOX}")
        if guess_column == 2:
            print(f"{BLUE_BOX}{guess_results}{BLUE_BOX}{BLUE_BOX}")
        if guess_column == 3:
            print(f"{BLUE_BOX}{BLUE_BOX}{guess_results}{BLUE_BOX}")
        if guess_column == 4:
            print(f"{BLUE_BOX}{BLUE_BOX}{BLUE_BOX}{guess_results}")
    else:
        print(f"{BLUE_BOX}{BLUE_BOX}{BLUE_BOX}{BLUE_BOX}")
    row_print = row_print + 1
if guess_row == boat_row and guess_column == boat_column:
    print("Hit! ")
if guess_row == boat_row and guess_column != boat_column:
    print("close! Correct row, wrong column. ")
if guess_row != boat_row and guess_column == boat_column:
    print("Close! Correct column, wrong row. ")
if guess_row != boat_row and guess_column != boat_column:
    print("Miss! ")

