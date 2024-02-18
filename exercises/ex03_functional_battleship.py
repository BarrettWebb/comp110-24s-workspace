"""Functional battleship exercise 03."""


__author__ = "730544769"
import random

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"
storage: str = ""
game_results: str = ""


def input_guess(grid_size: int, direction: str) -> int:
    """Input guess for game."""
    assert direction == "row" or direction == "column"
    if direction == "row":
        guess_row = int(input("Guess a row: "))
        guess_row = int(guess_row)
        if guess_row >= 1 and guess_row <= grid_size:
            print(guess_row)
        while guess_row < 1 or guess_row > grid_size:
            guess_row = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))
            guess_row = int(guess_row)
        return int(guess_row)
    if direction == "column":
        guess_column = int(input("Guess a column: "))
        guess_column = int(guess_column)
        if guess_column >= 1 and guess_column <= grid_size:
            print(guess_column)
        while guess_column < 1 or guess_column > grid_size:
            guess_column = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))
            guess_column = int(guess_column)
        return int(guess_column)
    return 0
    

def print_grid(grid_size: int, row_guess: int, guess_column: int, hit: bool) -> None:
    """Print grid."""
    if hit:
        game_results = RED_BOX
    else:
        game_results = WHITE_BOX
    row_print: int = 1
    while row_print <= grid_size:
        if row_print == row_guess:
            print(f"{BLUE_BOX * (guess_column - 1)}{game_results}{BLUE_BOX * (grid_size - guess_column)}")
        else:
            print(BLUE_BOX * grid_size)
        row_print += 1


def correct_guess(secret_row: int, secret_column: int, guess_row: int, guess_column: int) -> bool:
    """Correct guess."""
    if secret_row == guess_row and secret_column == guess_column:
        return True
    else:
        return False


def main(grid_size: int, secret_row: int, secret_column: int) -> None:
    """Main code of program."""
    number_turns: int = 1
    while number_turns <= 5:
        print(f"=== Turn {number_turns}/5 ===")
        guess_row: int = input_guess(grid_size, "row")
        guess_column: int = input_guess(grid_size, "column")
        hit: bool = correct_guess(secret_row, secret_column, guess_row, guess_column)
        print_grid(grid_size, guess_row, guess_column, hit)
        if hit:
            print("Hit! ")
            print(f"You won in {number_turns}/5 turns! ")
            number_turns += 5
        else:
            print("Miss! ")
            if number_turns == 5:
                print("X/5 - Better luck next time! ")
            number_turns += 1
    

if __name__ == "__main__":
    grid_size: int = random.randint(3, 5)
    main(grid_size, random.randint(1, grid_size), random.randint(1, grid_size))