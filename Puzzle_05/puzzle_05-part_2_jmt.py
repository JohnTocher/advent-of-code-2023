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
            assert len(range_parts) == 3, f"Unexpected input for mapping range at line {count_lines}"
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
    """Performs the lookup for a single map conversion
    
    input_value: integer
        the value to to map
    map_type: str
        the name of the map to use, for example:
        fertilizer-to-water
    """

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
    """Goes through succesive map conversions to determine the see location
    
    This is the functionality required in part 1 of the puzzle
    """

    current_value = seed_number
    for map_type in CONVERSION_ORDER:
        current_value = map_lookup(current_value, map_type)

    return current_value

def seed_to_location_ranges(input_ranges):
    """Goes through succesive map conversions to determine the next layers output ranges
    
    This is the functionality required in part 2 of the puzzle
    """

    ranges_to_map= input_ranges

    for map_type in CONVERSION_ORDER:
        print(f"Using map {map_type} for which has ranges: {ranges_to_map}")
        output_ranges = []
        while ranges_to_map:    # Still have ranges to process - will remove 1-1 maps
            test_range = ranges_to_map.pop()
            input_start = test_range[0]
            input_end = test_range[1]
            print(f"Handling range: {test_range}")
            map_solution_found = False
            for sub_map in map_data[map_type]:
                range_min = sub_map["source_start"]
                range_max = sub_map["source_end"]
                dest_start = sub_map["dest_start"]
                print(f"Testing input range {test_range} against map {range_min}:{range_max} to:{dest_start}...")
                if input_start >= range_min: # X >= A on diagram
                    if input_end <= range_max:    # Y <= B on diagram, direct map - case 6 
                        print("Input range mapped 1-1")
                        output_start = input_start - range_min + dest_start
                        output_end = input_end - range_min + dest_start
                        output_ranges.append([output_start, output_end])
                        map_solution_found = True
                        print(f"Got direct output ranges: {output_ranges}")
                        break   # Dont need to check additional sub-maps
                    elif range_max >= input_start: # B > X on diagram - case 2
                        print("Input range split across X")
                        ranges_to_map.append([input_start,range_max])
                        ranges_to_map.append([range_max +1, input_end])
                        break   # Don't need to check additional sub-maps
                    else:   # No overlap case 1
                        pass
                elif input_end < range_min: # Y < A on diagram
                    pass    # No overlap in ranges - case 5

                elif input_end <= range_max:    # Case 4
                        ranges_to_map.append([input_start,range_min])
                        ranges_to_map.append([range_min + 1, input_end])
                        break   # Don't need to check additional sub-maps
                else:   # Case 3 
                    ranges_to_map.append([input_start,range_min -1])
                    ranges_to_map.append([range_min, range_max])
                    ranges_to_map.append([range_max + 1, input_end])
                    break   # Don't need to check additional sub-maps

            # Maps all scanned
            print("sub-maps all scanned")
            if not map_solution_found:
                output_ranges.append([input_start, input_end])
                print(f"No matches found, appending as is: {[input_start, input_end]}")
        
        # No more ranges to map - all processed
        ranges_to_map = output_ranges
        ranges_to_map.sort()
        print("Ranges at this level all processed")
        print(f"New ranges: {output_ranges}")




            

    return output_ranges


# Main program flow begins here

map_data = read_map_data()  # Global variable, used in functions!

seed_input_data = map_data["seeds"]    # Seed list calculated as per part 1 of the puzle
seed_ranges = list()

for seed_index in range(0,len(seed_input_data), 2):
    seed_start = seed_input_data[seed_index]
    seed_end = seed_start + seed_input_data[seed_index + 1] - 1
    seed_range = (seed_start, seed_end)
    seed_ranges.append(seed_range)
    
seed_ranges.sort()
print(f"seed_ranges are {seed_ranges}")

final_ranges = seed_to_location_ranges(seed_ranges)

exit(0)

location_list = list()
for seed_value in old_seeds:
    seed_location = seed_to_location(seed_value)
    location_list.append(seed_location)

print(f"Lowest location number is {min(location_list)}")
print(f"Expected answer for John's input data is {42}")
