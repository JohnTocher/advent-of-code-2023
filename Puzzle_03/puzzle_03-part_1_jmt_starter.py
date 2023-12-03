""" Advent of code 2023 - Puzzle 03

    https://adventofcode.com/2023/day/3

    John Tocher     
    Starter code for puzzle 03
"""

INPUT_FILE_NAME = "puzzle_03_input_01_sample.txt"


def read_schematic_lines():
    """Reads the input data and returns a list of text lines"""

    schematic_lines = list()
    for each_line in open(INPUT_FILE_NAME, "r").readlines():
        schematic_lines.append(each_line.strip())  # Remove EOLs

    return schematic_lines


def get_symbol_locations(schematic_lines, gears_only=False):
    """Iterates over the schematic, finds co-ords of symbols

    Will return a list of tuples
    coordinates will be (col_num, row_num)
    increasing left to right and top to bottom
    """

    list_of_points = list()

    row_num = 0
    for single_line in schematic_lines:
        for col_num in range(0, len(single_line)):
            single_char = single_line[col_num : col_num + 1]
            if single_char == ".":
                pass
            elif single_char.isdigit():
                pass
            elif gears_only and (single_char != "*"):
                pass
            else:
                this_point = (col_num, row_num)
                list_of_points.append(this_point)
        row_num += 1

    return list_of_points


def get_part_numbers(schematic_lines):
    """
    Iterates over the schematic, finds part numbers

    Will return a list of dictionaries
    Each dictionary will have two keys:
        "value": The part number, eg 123
        "locations": A list of tuples of (col_num, row_num)

    coordinates will be (col_num, row_num)
    increasing left to right and top to bottom
    """

    list_of_parts = list()

    row_num = 0
    for single_line in schematic_lines:
        digits_as_text = ""
        digit_locations = list()
        for col_num in range(0, len(single_line)):
            single_char = single_line[col_num : col_num + 1]
            finalise_this_part = False
            if single_char.isdigit():
                digits_as_text = f"{digits_as_text}{single_char}"
                digit_locations.append((col_num, row_num))
                if col_num == len(single_line) - 1:
                    finalise_this_part = True
            else:
                if digits_as_text:  # True if it has anything in it
                    finalise_this_part = True

            if finalise_this_part:
                this_num = int(digits_as_text)
                sch_dict = dict()
                sch_dict["locations"] = digit_locations
                sch_dict["value"] = this_num
                list_of_parts.append(sch_dict)
                digits_as_text = ""  # Clear the values - might multiple per line
                digit_locations = list()

        row_num += 1

    return list_of_parts


schematic_lines = read_schematic_lines()
gear_locs = get_symbol_locations(schematic_lines)
print(f"Found {len(gear_locs)} symbols from {len(schematic_lines)} lines")

part_data = get_part_numbers(schematic_lines)
print(f"Found {len(part_data)} part numbers from {len(schematic_lines)} lines")
