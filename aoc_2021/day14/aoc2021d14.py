# https://adventofcode.com/2021/day/14

from os import pipe
import pathlib
import time
from collections import defaultdict
from collections import Counter

script_path = pathlib.Path(__file__).parent
input = script_path / "input.txt"  # 2447 / 3018019237563
input_test = script_path / "test.txt"  # 1588 / 2188189693529


def parse(puzzle_input):
    """Parse input"""

    with open(puzzle_input, "r") as file:
        polymer, instructions = file.read().split("\n\n")
        rules = defaultdict()
        tmp = [[r for r in pair.split(" -> ")] for pair in instructions.split("\n")]
        for l, r in tmp:
            rules[l] = r

        # print(polymer)
        # print(rules)

    return polymer, rules


def part1(polymer, insertion_rules, steps=10):
    """Solve part 1"""

    current_polymer = polymer
    # print(insertion_rules)

    for i in range(steps):
        # print("Polymer = ",current_polymer)
        next_polymer = ""

        for c in range(len(current_polymer) - 1):
            check = current_polymer[c] + current_polymer[c + 1]
            # print('\n',c, current_polymer, check)

            if check in insertion_rules.keys():
                insertion = check[0] + insertion_rules[check]  # + check[1]
            else:
                insertion_rules = check[0]

            next_polymer = next_polymer + insertion

            # print(next_polymer)
        next_polymer = next_polymer + current_polymer[-1]

        # print(current_polymer,' > ', next_polymer)
        current_polymer = next_polymer
        # print('\nstep end',i,len(current_polymer))

    char_count = Counter(current_polymer)
    # print(char_count)
    answer = max(char_count.values()) - min(char_count.values())

    return answer


def next2Char(polymer):
    for i in range(len(polymer) - 1):
        yield polymer[i] + polymer[i + 1]


def part2(polymer, insertion_rules, steps=10):
    """Solve part 2"""

    last_char = polymer[-1]
    polyCombis = defaultdict()

    # dict with the new insertion pair combinations rather than mapping
    for k, v in insertion_rules.items():
        polyCombis[k] = (k[0] + v, v + k[1])
    # print(polyCombis) # defaultdict(None, {'CH': ('CB', 'BH'), 'HH': ('HN', 'NH'),

    # a = ("John", "Charles", "Mike")
    # x = zip(a, a[1:])
    # ('John', 'Charles'), ('Charles', 'Mike'))

    polymerCounts = defaultdict(int)
    for pair in next2Char(polymer):
        polymerCounts[pair] += 1
    # print(polymerCounts) # defaultdict(<class 'int'>, {'NN': 1, 'NC': 1, 'CB': 1})

    for i in range(steps):
        # print('\nstep', i)

        nextPolymerCounts = defaultdict(int)

        for pPair in polymerCounts:
            newCombi = polyCombis.get(pPair)
            # print('pPair',pPair) # eg pPair NN
            # print('newCombi',newCombi)  #newCombi ('KN', 'NH')

            if newCombi:
                # increase each of the combinations that will now be added
                count = polymerCounts[pPair]
                nextPolymerCounts[newCombi[0]] += count
                nextPolymerCounts[newCombi[1]] += count
            else:
                # With combinations then increment the pPair counter only
                nextPolymerCounts[pPair] = polyCombis[pPair]
            # print(nextPolymerCounts)

        polymerCounts = nextPolymerCounts

    char_count = defaultdict(int)
    for k, n in polymerCounts.items():
        char_count[k[0]] += n

    char_count[last_char] += 1
    # print(char_count)
    answer = max(char_count.values()) - min(char_count.values())

    return answer


def solve(puzzle_input, run="Solution"):
    """Solve the puzzle for the given input"""
    times = []

    polymer, insertion_rules = parse(puzzle_input)

    times.append(time.perf_counter())
    solution1 = part1(polymer, insertion_rules, 10)
    times.append(time.perf_counter())
    solution2 = part2(polymer, insertion_rules, 40)
    times.append(time.perf_counter())

    print(f"{run} 1: {str(solution1)} in {times[1]-times[0]:.4f}s")
    print(f"{run} 2: {str(solution2)} in {times[2]-times[1]:.4f}s")
    print(f"\nExecution total: {times[-1]-times[0]:.4f} seconds")

    return solution1, solution2, times


if __name__ == "__main__":
    print("\nAOC")

    tests = solve(input_test, run="Test")

    print()
    solutions = solve(input)
