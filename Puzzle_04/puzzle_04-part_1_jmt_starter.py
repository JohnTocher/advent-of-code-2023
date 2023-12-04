""" Advent of code 2023 - Puzzle 04

    https://adventofcode.com/2023/day/4

    John Tocher     
    Starter code for puzzle 04
"""

INPUT_FILE_NAME = "puzzle_04_input_01_sample.txt"


def read_game_results():
    """Iterates over the cards and returns a list of results, each a dictionary"""

    result_dict = dict()

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
            card_detail["card_number"] = card_number
            card_detail["win_list"] = winning_numbers  # left side of |
            card_detail["have_list"] = numbers_we_have  # right side of |, to check
            card_detail["count"] = 1

            extra_cards = 0
            for each_winner in winning_numbers:
                if each_winner in numbers_we_have:
                    extra_cards += 1

            card_detail["wins"] = extra_cards

            # Save our results dictionary to the list
            result_dict[card_number] = card_detail

    return result_dict


all_cards = read_game_results()


print(f"Read {len(all_cards)} card details")
