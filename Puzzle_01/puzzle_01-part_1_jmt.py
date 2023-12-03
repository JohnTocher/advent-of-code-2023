""" Advent of code 2023 - Puzzle 01

    https://adventofcode.com/2023/day/1

    John Tocher     
    Solution to puzzle 01 part 1
"""

INPUT_FILE_NAME = "puzzle_01_input_01_full_jmt.txt"

answer_total = 0
count_lines = 0

for single_line in open(INPUT_FILE_NAME, "r").readlines():
    count_lines += 1
    clean_line = single_line.strip()
    line_length = len(clean_line)

    # Process the line in the foreward direction
    for char_pos in range(0, line_length):
        this_char = clean_line[char_pos : char_pos + 1]
        if this_char.isdigit():
            this_number = (
                int(this_char) * 10
            )  # Convert our text to a number and make it the tens value
            break  # dont process any more characters in this forward direction

    for char_pos in range(line_length, 0, -1):
        this_char = clean_line[char_pos - 1 : char_pos]
        if this_char.isdigit():
            this_number += int(
                this_char
            )  # Convert our text to a number and add it to our total
            break  # dont process any more characters in the backward direction, wer're done!

    answer_total += this_number

print(f"Calculated a total of {answer_total} over {count_lines} lines")
print(f"Correct answer for John's input data was {54159}")
