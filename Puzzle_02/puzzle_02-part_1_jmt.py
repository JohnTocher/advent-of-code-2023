""" Advent of code 2023 - Puzzle 02

    https://adventofcode.com/2023/day/2

    John Tocher     
    Solution to puzzle 02 part 1
"""

INPUT_FILE_NAME = "puzzle_02_input_01_full_jmt.txt"
CUBE_COLOURS = ["red", "green", "blue"]


def read_game_records():
    """Reads the records line by line, returning a list of dictionaries

    each list element is dictionary of {colour:count}
    the list index will be the game id, as long as our data includes
    entries for every game.  This seems to be the case here.
    """

    result_list = list()

    count_games = 0
    for input_line in open(INPUT_FILE_NAME).readlines():
        count_games += 1
        game_parts = input_line.split(":")  # Separates the game name and the details
        game_name = game_parts[0].strip()  # strip not required for clean input data
        sub_games = game_parts[1].strip().split(";")
        # sub games is now  a list of csv text (number, colour) for this game
        count_sub_games = 0
        cube_counts = dict()  # Empty dictionary
        for sub_game in sub_games:
            count_sub_games += 1
            sub_game_parts = sub_game.split(":")
            sub_game_cubes = sub_game.split(",")
            for each_cube in sub_game_cubes:
                clean_cube_data = each_cube.strip()
                cube_parts = clean_cube_data.split(" ")  # Split from "N colour"
                cube_count = int(cube_parts[0])
                cube_colour = cube_parts[1].strip()  # Ensure no extra spaces etc
                if cube_colour in cube_counts:  # Already seen this colour
                    new_count = max(cube_counts[cube_colour], cube_count)
                else:
                    new_count = cube_count
                cube_counts[cube_colour] = new_count  # Update or create the value
            # print(f"Cube counts for game {count_games:03}: {cube_counts}")

        result_list.append(cube_counts)

    return result_list


game_records = read_game_records()
print(f"It looks like I have {len(game_records)} records")

# This is not the most compact way to declare and fill this dictionary, but it's clear in this case
max_values = dict()
max_values["red"] = 12
max_values["green"] = 13
max_values["blue"] = 14

game_id = 0
id_sum = 0

for test_game in game_records:
    game_id += 1  # Our games are in order in the list, so this is OK, if not ideal
    game_is_possible = True
    for test_colour in CUBE_COLOURS:
        if test_game[test_colour] > max_values[test_colour]:
            game_is_possible = False

    if game_is_possible:
        id_sum += game_id

print(f"Sum of ids for possible games is {id_sum}")
print(f"Correct answer for John's input data was {2879}")
