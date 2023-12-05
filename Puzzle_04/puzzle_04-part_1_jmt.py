""" Advent of code 2023 - Puzzle 04

    https://adventofcode.com/2023/day/4

    John Tocher     
    Solution to puzzle 04 part 1
"""

INPUT_FILE_NAME = "puzzle_04_input_01_full_jmt.txt"


def read_game_results():
    """Iterates over the cards and returns a list of results, each a dictionary"""

    result_list = list()

    with open(INPUT_FILE_NAME, "r") as input_file:
        for single_card in input_file.readlines():
            card_detail = dict()  # used for storing all data, might not be necessary!

            card_parts = single_card.split("|")
            pos_colon = card_parts[0].find(":")
            card_number = int(card_parts[0][4:pos_colon])

            # The next two lines have a replace function to avoid the split function
            # resulting in empty entries in the list where there were two spaces
            card_win_text = card_parts[0][pos_colon + 1 :].strip().replace("  ", " ")
            card_have_text = card_parts[1].strip().replace("  ", " ")

            # We can then safely turn our list of numbers as text into a list of integers
            # with a list comprehension
            winning_numbers = [int(text_num) for text_num in card_win_text.split(" ")]
            numbers_we_have = [int(text_num) for text_num in card_have_text.split(" ")]

            # Store of values in a dictionary
            card_detail["number"] = card_number
            card_detail["winners"] = winning_numbers
            card_detail["have"] = numbers_we_have

            # Calculate the number of winning numbers we have
            num_winners = 0
            card_points = 0
            for each_winner in winning_numbers:
                if each_winner in numbers_we_have:
                    num_winners += 1

            if num_winners:
                card_points = pow(2, num_winners - 1)
                # This is a way to write 2 to the power of (num_winners-1)
                # You can also use ** for exponents, but I thought this might be
                # confusing for the hard core C programmers. No pointers here
            card_detail["points"] = card_points

            # Save our results dictionary to the list
            result_list.append(card_detail)

            # Reproduce the input format (almost) for a sanity check
            # print(f"Card {card_number}:{card_winners} | {card_numbers} for {card_points} points")

    return result_list


game_results = read_game_results()
total_points = 0
for each_result in game_results:
    total_points += each_result["points"]

print(f"Total points for {len(game_results)} cards was {total_points}")
print(f"Expected result for John's data was {24175}")
