""" Advent of code 2023 - Puzzle 05

    https://adventofcode.com/2023/day/5

    John Tocher     
    Solution to puzzle 05 part 2
"""

INPUT_FILE_NAME = "puzzle_05_input_01_sample.txt"

CONVERSION_ORDER = [
    "seed-to-soil",
    "soil-to-fertilizer",
    "fertilizer-to-water",
    "water-to-light",
    "light-to-temperature",
    "temperature-to-humidity",
    "humidity-to-location",
]


def read_map_data():
    """Reads the map data

    Returns a dictionary where the key is either the map name or 'seeds'

    the seeds entry will be a list of seeds

    the map type entries will be an input range (min, max)
    and a starting point for the output range

    """

    map_data = dict()
    current_map = False
    map_list = list()
    finish_map = False
    count_lines = 0

    for data_line in open(INPUT_FILE_NAME, "r").readlines():
        clean_line = data_line.strip()
        count_lines += 1
        if clean_line.startswith("seeds:"):
            seed_text = clean_line[7:]
            seed_list = [int(seed_num) for seed_num in seed_text.split(" ")]
            map_data["seeds"] = seed_list
        elif clean_line == "":
            if current_map:
                finish_map = True
                current_map = False
        elif clean_line.endswith("map:"):
            assert not current_map, "Shouldn't get new map before finishing last one!"
            current_map = clean_line.split(" ")[0]  # Left of space
            map_data[current_map] = list()
        else:
            # Should be a list of three numbers - output start, input start, range
            range_parts = [int(range_part) for range_part in clean_line.split(" ")]
            map_details = dict()
            map_details["source_start"] = range_parts[1]
            map_details["source_end"] = range_parts[1] + range_parts[2] - 1
            map_details["dest_start"] = range_parts[0]
            map_data[current_map].append(map_details)

    if current_map:
        # Handle the final line, which doesn't have the usual empty line following it
        # It would have been easier to manually add a blank line at the end!
        range_parts = [int(range_part) for range_part in clean_line.split(" ")]
        map_details = dict()
        map_details["source_start"] = range_parts[1]
        map_details["source_end"] = range_parts[1] + range_parts[2] - 1
        map_details["dest_start"] = range_parts[0]
        map_data[current_map].append(map_details)
        # map_list.append(range_parts)

    return map_data


def map_lookup(input_value, map_type):
    """Performs the lookup for a single map conversion"""

    output_value = input_value

    # print(f"Doing lookup for {input_value} in {map_type}")
    maps_for_type = map_data[map_type]
    for sub_map in maps_for_type:
        range_min = sub_map["source_start"]
        range_max = sub_map["source_end"]
        dest_start = sub_map["dest_start"]
        if input_value >= range_min and input_value <= range_max:
            output_value = (input_value - range_min) + dest_start
            break  # don't need to keep searching

    return output_value


def seed_to_location(seed_number):
    """Goes through succesive map conversions to determine the see location"""

    current_value = seed_number
    for map_type in CONVERSION_ORDER:
        current_value = map_lookup(current_value, map_type)

    return current_value


map_data = read_map_data()  # Global variable, used in functions!

just_seeds = map_data["seeds"]
print(f"Seeds: {just_seeds}")

# test_seed = just_seeds[0]
# final_location = seed_to_location(test_seed)
# print(f"Seed {test_seed} to location {final_location}")

location_list = list()
for seed_value in just_seeds:
    seed_location = seed_to_location(seed_value)
    location_list.append(seed_location)

print(f"Lowest location number is {min(location_list)}")
print(f"Expected answer for John's input data is {579439039}")
