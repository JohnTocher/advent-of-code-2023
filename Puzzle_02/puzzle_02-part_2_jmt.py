""" Advent of code 2023 - Puzzle 02

    https://adventofcode.com/2023/day/2

    John Tocher     
    Solution to puzzle 02 part 2
"""

INPUT_FILE_NAME = "puzzle_02_input_01.txt"
CUBE_COLOURS = ["red", "green", "blue"]


def calc_cube_power(cube_data):
    """Calculates the cube power"""

    power_product = 1

    for cube_colour in CUBE_COLOURS:
        # this_num = cube_data.get(cube_colour, 0)  # Use 0 if not present
        this_num = cube_data[cube_colour]
        power_product *= this_num

    return power_product


def read_game_records():
    """Reads the records line by line, returning a list of dictionaries

    each list element is dictionary of {colour:count}
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
            # print(f">> Game {count_games} sub game {count_sub_games} is {sub_game}")
            sub_game_cubes = sub_game.split(",")
            # print(f"sub_game_cubes: {sub_game_cubes}")
            for each_cube in sub_game_cubes:
                clean_cube_data = each_cube.strip()
                cube_parts = clean_cube_data.split(" ")  # Split from "N colour"
                # print(f"  >> {cube_parts=}")
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

power_sum = 0

for test_game in game_records:
    power_set = calc_cube_power(test_game)
    power_sum += power_set

print(f"Sum of powers is {power_sum}")
