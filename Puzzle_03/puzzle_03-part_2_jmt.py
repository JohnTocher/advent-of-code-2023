""" Advent of code 2023 - Puzzle 03

    https://adventofcode.com/2023/day/3

    John Tocher     
    Solution to puzzle 03 part 2
"""

INPUT_FILE_NAME = "puzzle_03_input_01_full_jmt.txt"


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


def filter_schematic(symbol_locations, part_data):
    """
    Iterates through all parts, checking if they are near symbols

    returns a list of doctionaries, in the same form as part_data
    This one is no longer needed in this solution, but I've left it
    in place for reference
    """

    valid_parts = list()

    for single_part in part_data:
        part_value = single_part["value"]
        part_locations = single_part["locations"]

        part_is_valid = False
        for digit_loc in part_locations:
            for symbol_loc in symbol_locations:
                delta_row = abs(digit_loc[1] - symbol_loc[1])
                if delta_row < 2:  # Same or adjance rows
                    delta_col = abs(digit_loc[0] - symbol_loc[0])
                    if delta_col < 2:
                        part_is_valid = True

            if part_is_valid:
                part_dict = dict()
                part_dict["locations"] = part_locations
                part_dict["value"] = part_value
                valid_parts.append(part_dict)
                break  # Don't need to process further digit locations for this part

    return valid_parts


def filter_gears(gear_locations, part_data):
    """
    Iterates through all gears, checking if they are near exactly two part numbers

    returns a list of lists, each sub-list being a list of part numbers
    filtered to only include cases where there were two results
    The gear locations are assumed to be already correct
    """

    valid_gears = list()

    for gear_loc in gear_locations:
        part_list = list()
        for part_detail in part_data:
            part_is_valid = False
            for digit_data in part_detail["locations"]:
                delta_row = abs(digit_data[1] - gear_loc[1])
                if delta_row < 2:  # Same or adjacent rows
                    delta_col = abs(digit_data[0] - gear_loc[0])
                    if delta_col < 2:
                        part_is_valid = True
            if part_is_valid:
                part_list.append(part_detail["value"])
        if len(part_list) == 2:
            valid_gears.append(part_list)

    return valid_gears


# Main program logic

schematic_lines = read_schematic_lines()
gear_locs = get_symbol_locations(schematic_lines, gears_only=True)
print(f"Found {len(gear_locs)} gear symbols from {len(schematic_lines)} lines")

part_data = get_part_numbers(schematic_lines)
print(f"Found {len(part_data)} parts from {len(schematic_lines)} lines")

valid_gears = filter_gears(gear_locs, part_data)
print(f"Found {len(valid_gears)} valid gears")

gear_ratio_sum = 0
for single_gear in valid_gears:
    gear_ratio_sum += single_gear[0] * single_gear[1]

print(f"Sum of valid part gear rations is {gear_ratio_sum}")
print(f"Expected answer for John's input data is {81166799}")
