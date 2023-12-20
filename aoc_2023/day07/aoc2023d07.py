# https://adventofcode.com/2023/day/7

import pathlib
import time
from collections import Counter

script_path = pathlib.Path(__file__).parent
soln_file = script_path / "input.txt"  # 251216224 / 250825971
test_file = script_path / "test.txt"  # 6440 / 5905
test_file2 = script_path / "test2.txt"  # 6592 / 6839

# Use HEX and string translation
# https://www.geeksforgeeks.org/python-string-translate/

# Use sort with custom comparison
# https://learnpython.com/blog/python-custom-sort-function/

card_table = str.maketrans("TJQKA", "ABCDE")

# Hint from the internet on translation still works just use 0
# card_table_jk = str.maketrans("TJQKA", "A0CDE")
# didnt use - would have had to read input again, just made another dict in p2


def parse(puzzle_input):
    """Parse input"""

    hands = {}

    with open(puzzle_input, "r") as file:
        #  Read each line (split \n) and form a list of strings
        lst = file.read().split("\n")

    for l in lst:
        cards, bet = l.split()
        card_trans = cards.translate(card_table)
        hands[card_trans] = int(bet)

    print(hands)

    return hands


def check_hands(h):
    hand_card_counts = Counter(h)
    print(Counter(hand_card_counts))

    # Counts of different types of cards will show what type of hand
    card_variation = len(hand_card_counts)

    # Counter: it is a dict (or like one).
    # elements, most_common, subtract, total,

    # need to order hands on card points
    # what to return, ranking, and....

    hand_counts_sorted = sorted(hand_card_counts.values(), reverse=True)

    if card_variation == 1:
        # AAAAA
        print("5-of-a-kind")
        return (9, hand_counts_sorted)

    if card_variation == 2:
        # AAAA4  AAA44
        if 4 in hand_card_counts.values():
            print("4-of-a-kind")
            return (8, hand_counts_sorted)

        print("fullhouse")
        return (7, hand_counts_sorted)

    if card_variation == 3:
        # hmm this cand be fullhouse OR two pairs
        # AAA45  AA445
        if 3 in hand_card_counts.values():
            print("triple")
            return (6, hand_counts_sorted)

        # if 2 in card_variation.values():  # ???
        print("two pairs")
        return (5, hand_counts_sorted)

    if card_variation == 4:
        print("one pair")
        return (4, hand_counts_sorted)

    # Means 5 different cards
    return (0, hand_counts_sorted)


def check_hands_jk(h):
    # Jokers are now 0 after changing them from B
    hand_card_counts = Counter(h)
    print(hand_card_counts)

    # Counter can default if missing, means I can lose the IF checks and ELSE and do in one line.
    are_there_jokers = hand_card_counts.pop("0", 0)
    print("Jokers:", are_there_jokers)

    hand_counts_sorted = sorted(hand_card_counts.values(), reverse=True)

    # This was the error / over-complication. I added in jokers in the wrong place
    # Can just add them here after removing, sorting, add to the first indexable item
    hand_counts_sorted[0] += are_there_jokers

    # Counts of different types of cards will show what type of hand - now based on JK counts
    card_variation = len(hand_counts_sorted)
    print(card_variation, ":", hand_counts_sorted)

    #  Value checks on sorted list NOT Counter so I missed this when copy/pasting p1
    if card_variation == 1:
        # AAAAA
        print("5-of-a-kind")
        return (9, hand_counts_sorted)

    if card_variation == 2:
        # AAAA4  AAA44
        if 4 in hand_counts_sorted:
            print("4-of-a-kind")
            return (8, hand_counts_sorted)

        print("fullhouse")
        return (7, hand_counts_sorted)

    if card_variation == 3:
        # hmm this cand be fullhouse OR two pairs
        # AAA45  AA445
        if 3 in hand_counts_sorted:
            print("triple")
            return (6, hand_counts_sorted)

        # if 2 in card_variation.values():  # ???
        print("two pairs")
        return (5, hand_counts_sorted)

    if card_variation == 4:
        print("one pair")
        return (4, hand_counts_sorted)

    # Means 5 different cards
    return (1, hand_counts_sorted)


def part1(data):
    """Solve part 1"""

    print("\nPart 1")
    print(data)

    all_hands_total = 0

    hands = []

    for h, b in data.items():
        hand_val, hand_counts_sorted = check_hands(h)
        print(h, b, ":", hand_val, hand_counts_sorted)

        # Could we put the function in below and skip variables? Try
        hands.append((h, b, hand_val, hand_counts_sorted))

    all_hands_in_order = sorted(
        hands, key=lambda x: (x[2], x[3], x[0])
    )  # , reverse=True)
    print(all_hands_in_order)

    # Bet * rank, all added together
    # Doh!  read instricutions - its the rank (so the order) and therefore not the value of the hands (slaps head),
    # need to use enumerate and why the order of the list is important for this
    for r, (_, b, v, _) in enumerate(all_hands_in_order):
        all_hands_total += (r + 1) * b

    return all_hands_total


def part2(data):
    """Solve part 2"""
    # So the hint here is to realise that J should be changed to whatever card
    # has the highest frequency (anything else just weakens the hands)

    # So need to find jokers, and remove, then calculate counts, and add to the first one the jokers.

    print("\nPart 2")
    print(data)

    part2_hands_data = {}

    # Dont need to translate, or I would have to read the input again.
    # Create a new dict and convert the keys as go
    # Probably some clever one-liner here but cant work it out
    for h, b in data.items():
        part2_hands_data[h.replace("B", "0")] = b

    print(part2_hands_data)

    hands = []

    for h, b in part2_hands_data.items():
        print("\nh:", h, "\tb:", b)
        # Ah the test that is not in the tests
        # Thanks redit thread for test2 set of data and answers
        if h == "00000":
            print("---5 Jokers---")
            hand_val, hand_counts_sorted = (9, [5])
        else:
            hand_val, hand_counts_sorted = check_hands_jk(h)

        # Could we put the function in below and skip variables? Try
        hands.append((h, b, hand_val, hand_counts_sorted))

    # print()
    # print(hands)
    # for h in hands:
    #     print(h[0], h[1], h[2], h[3])

    all_hands_in_order = sorted(
        hands, key=lambda x: (x[2], x[3], x[0])
    )  # , reverse=True)

    # print(all_hands_in_order)
    # for h in all_hands_in_order:
    #     print(h[0], h[1], h[2], h[3])

    all_hands_total = 0
    # Bet * rank, all added together
    # Doh!  read instricutions - its the rank (so the order) and therefore not the value of the hands (slaps head),
    # need to use enumerate and why the order of the list is important for this
    for r, (_, b, v, _) in enumerate(all_hands_in_order):
        all_hands_total += (r + 1) * b

    return all_hands_total


def solve(puzzle_input, run="Solution"):
    """Solve the puzzle for the given input"""
    times = []

    data = parse(puzzle_input)

    times.append(time.perf_counter())
    solution1 = part1(data)
    times.append(time.perf_counter())
    solution2 = part2(data)
    times.append(time.perf_counter())

    print(f"{run} 1: {str(solution1)} in {times[1]-times[0]:.4f}s")
    print(f"{run} 2: {str(solution2)} in {times[2]-times[1]:.4f}s")
    print(f"\nExecution total: {times[-1]-times[0]:.4f} seconds")

    return solution1, solution2, times


if __name__ == "__main__":
    print("\nAOC")

    tests = solve(test_file, run="Test")
    tests2 = solve(test_file2, run="Test2")

    print()
    solutions = solve(soln_file)
