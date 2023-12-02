""" Advent of code 2023 - Puzzle 02

    https://adventofcode.com/2023/day/2

    John Tocher     
    Starter for puzzle 02
    Reads the sample text from the puzzle description, but doesn't count anything properly!
"""

INPUT_FILE_NAME = "puzzle_02_input_01_sample.txt"

CUBE_COLOURS = ["red", "green", "blue"]

# Incomplete!
# Read the game records


def read_game_records():
    """Reads the records line by line, returning a list of dictionaries

    each list element is dictionary of {colour:count}

    """

    result_list = list()

    count_games = 0
    for input_line in open(INPUT_FILE_NAME).readlines():
        count_games += 1
        game_parts = input_line.split(":")  # Separates the game name and the details
        game_name = game_parts[
            0
        ].strip()  # strip may not be required for clean input data
        sub_games = (
            game_parts[1].strip().split(";")
        )  # list of csv text (number, colour) for this game
        count_sub_games = 0
        for sub_game in sub_games:
            count_sub_games += 1
            sub_game_parts = sub_game.split(":")
            game_name
            print(f"Game {count_games} sub game {count_sub_games} is {sub_game}")

    return result_list


game_records = read_game_records()
print(f"It looks like I have {len(game_records)} records")
