""" Advent of code 2023 - Puzzle 01

    https://adventofcode.com/2023/day/1

    John Tocher     
    Solution to puzzle 01 part 2
"""

INPUT_FILE_NAME = "puzzle_01_input_01.txt"

DIGITS_AS_TEXT = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]

answer_total = 0
count_lines = 0

for single_line in open(INPUT_FILE_NAME, "r").readlines():
    count_lines += 1
    clean_line = single_line.strip()
    line_length = len(clean_line)
    # Process the line in the forward direction
    for char_pos in range(0, line_length):  # Outer for loop - whole line left to right
        this_char = clean_line[char_pos : char_pos + 1]
        if this_char.isdigit():
            this_number = (
                int(this_char) * 10
            )  # Convert our text to a number and make it the tens value
            break  # dont process any more characters in this forward direction
        else:
            part_to_check = clean_line[char_pos:]  # This position until the end
            digit_count = 0
            found_from_left = False
            for text_for_digit in DIGITS_AS_TEXT:
                digit_count += 1
                if part_to_check.startswith(text_for_digit):
                    this_number = digit_count * 10
                    found_from_left = True
                    break
            if found_from_left:
                break  # We need to exit from our outer left to right for loop

    for char_pos in range(line_length, 0, -1):  # Outer loop - whole line right to left
        this_char = clean_line[char_pos - 1 : char_pos]
        if this_char.isdigit():
            # Convert our text to a number and add it to our total
            this_number += int(this_char)
            break  # dont process any more characters in the backward direction, wer're done!
        else:
            part_to_check = clean_line[char_pos - 1 :]  # This position until the end
            digit_count = 0
            found_from_right = False
            for text_for_digit in DIGITS_AS_TEXT:
                digit_count += 1
                if part_to_check.startswith(text_for_digit):
                    this_number += digit_count
                    found_from_right = True
                    break
            if found_from_right:
                break  # Need to exit the right-to-left outer foor loop

    answer_total += this_number
    # print(f"This line {this_number} Total: {answer_total}")

print(f"Calculated a total of {answer_total} over {count_lines} lines")
