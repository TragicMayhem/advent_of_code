# https://adventofcode.com/2015/day/15

import pathlib
import time
import timeit
from collections import defaultdict
import itertools
import math
from pprint import pprint

script_path = pathlib.Path(__file__).parent
input = script_path / "input.txt"  #  # 21367368 / 1766400
input_test = (
    script_path / "test.txt"
)  # 44 B 65 C score is 62842880 / 40 B and 60 C = 500 calories and score 57600000


ingredients = defaultdict(dict)
properties = [
    "capacity",
    "durability",
    "flavor",
    "texture",
    "calories",
]  # Ignore calories in part 1 calc of the score


def parse(puzzle_input):
    """Parse input"""
    with open(puzzle_input, "r") as file:
        data = file.read().replace(": ", ",").replace(", ", ",").split("\n")
        data = [d.split(",") for d in data]

        ingredients_input = defaultdict(dict)
        for item in data:
            name = item[0]

            for i in range(1, len(item)):
                tmp = item[i].split(" ")
                ingredients_input[name].update({tmp[0]: int(tmp[1])})

    return ingredients_input


def calc_combinations(target, splits):
    """
    range 1 to target for each of the splits to form all combinations
    remove all that are not eq target
    return the list
    """
    output = []
    results = list(itertools.permutations(range(1, target + 1), splits))

    for i in results:
        if sum(i) == target:
            output.append(i)

    return output


def process_combinations(ingredients):
    max_teaspoons = 100
    # keep_combinations = []

    number_of_ingredients = len(ingredients.keys())
    names_of_ingredients = list(ingredients.keys())
    keep_combinations = calc_combinations(max_teaspoons, number_of_ingredients)

    pprint(ingredients)
    print("No. ingredients:", number_of_ingredients, "List:", names_of_ingredients)

    all_answers = []
    valid_property_lists = []

    for mix in keep_combinations:
        current_mix_list = []
        for i, teaspoons in enumerate(mix):
            prop_list = []

            for j in range(len(properties)):
                prop_list.append(
                    ingredients[names_of_ingredients[i]].get(properties[j], 0)
                    * teaspoons
                )

            current_mix_list.append(prop_list)

        # Use zip to to sum all the elements in each list together to get the answer for each property
        property_totals_list = [sum(i) for i in zip(*current_mix_list)]

        all_answers.append(property_totals_list)

        if all(i >= 0 for i in property_totals_list):
            valid_property_lists.append(property_totals_list)

    return valid_property_lists


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    times = []
    time_start = timeit.default_timer()

    ingredients = parse(puzzle_input)
    valid_list = process_combinations(ingredients)
    times.append(time.perf_counter())
    print(
        f"\nA. Time difference after calc_combinations :  {timeit.default_timer() - time_start:.4f}s"
    )

    print("\nPart 1")
    scores = []
    for a in valid_list:
        scores.append(math.prod(a[:-1]))  # Ignore calories in the score
    solution1 = max(scores)

    print("Number of filtered multiplied answers:", len(valid_list))
    print("\nThe highest score is:", solution1)

    print(
        f"\nB. Time difference after part 1 :  {timeit.default_timer() - time_start:.4f}s"
    )
    times.append(time.perf_counter())

    low_cal_cookies = []
    for i in range(len(valid_list)):
        if valid_list[i][4] == 500:
            low_cal_cookies.append(scores[i])

    solution2 = max(low_cal_cookies)
    print("Highest scoring low calories cookie: ", solution2)
    times.append(time.perf_counter())

    print(
        f"\nC. Time difference at the end :  {timeit.default_timer() - time_start:.4f}s"
    )

    return solution1, solution2, times


def runAllTests():
    print("\nTests\n")
    a, b, t = solve(input_test)
    print(f"Test1 Part 1: {a} in {t[1]-t[0]:.4f}s")
    print(f"      Part 2: {b} in {t[2]-t[1]:.4f}s")
    print(f"      Execution total: {t[-1]-t[0]:.4f} seconds")


if __name__ == "__main__":  # print()
    runAllTests()

    print(
        "\n\n....wait for it to run its computing a lot of permutations (approx 30-40s)"
    )

    sol1, sol2, times = solve(input)
    print("\nAOC")
    print(f"Solution 1: {str(sol1)} in {times[1]-times[0]:.4f}s")
    print(f"Solution 2: {str(sol2)} in {times[2]-times[1]:.4f}s")
    print(f"\nExecution total: {times[-1]-times[0]:.4f} seconds")
