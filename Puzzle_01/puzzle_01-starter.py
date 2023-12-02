""" Advent of code 2023 - Puzzle 01

    https://adventofcode.com/2023/day/1

    John Tocher     
    Starter code - a simple example - no spoilers!
"""

INPUT_FILE_NAME = "puzzle_01_input_01.txt"

# Parts one and two use the same data input, but there are also two 'sample' data sets
# extracted from the puzzle descriptions on the web site
# which might be useful if you want to check your output on a smaller data set

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
    this_number = 0
    # print(f"Line {count_lines:04} value is {this_number} Total: {answer_total}")

print(f"Calculated a total of {answer_total} over {count_lines} lines")
