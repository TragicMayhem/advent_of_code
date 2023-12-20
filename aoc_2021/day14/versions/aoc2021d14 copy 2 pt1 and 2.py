# https://adventofcode.com/2021/day/14

from os import pipe
import pathlib
import time
from collections import defaultdict
from collections import Counter

script_path = pathlib.Path(__file__).parent
soln_file = script_path / "input.txt"  # 2447 /
test_file = script_path / "test.txt"  # 1588


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


def loopPolymer(polymer, rules):
    c = 0
    next_polymer = ""

    while c < len(polymer) - 1:
        check = polymer[c : c + 1]

        if check in rules.keys():
            insertion = check[0] + rules[check]
        else:
            insertion = check[0]

        c += 1
        next_polymer = next_polymer + insertion

    next_polymer = next_polymer + polymer[-1]

    return next_polymer


def next2Char(polymer):
    for i in range(len(polymer) - 1):
        yield polymer[i] + polymer[i + 1]


def part2(polymer, insertion_rules, steps=10):
    """Solve part 2"""
    print("PART 2")
    current_polymer = polymer

    last_char = current_polymer[-1]
    polyCombis = defaultdict()

    # dict with the new insertion pair combinations rather than mapping
    for k, v in insertion_rules.items():
        polyCombis[k] = (k[0] + v, v + k[1])

    print(polyCombis)  # defaultdict(None, {'CH': ('CB', 'BH'), 'HH': ('HN', 'NH'),

    # tally = Counter(current_polymer)
    # a = ("John", "Charles", "Mike")
    # x = zip(a, a[1:])
    # ('John', 'Charles'), ('Charles', 'Mike'))

    polyCombiCount = defaultdict(int)

    for pair in next2Char(polymer):
        polyCombiCount[pair] += 1

    print(polyCombiCount)  # defaultdict(<class 'int'>, {'NN': 1, 'NC': 1, 'CB': 1})

    for i in range(steps):
        print("\nstep", i)

        nextPolymerCounts = defaultdict(int)

        for pPair in polyCombiCount:
            newCombi = polyCombis.get(pPair)
            print("pPair", pPair)
            print("newCombi", newCombi)

            if newCombi:
                count = polyCombiCount[pPair]
                print(pPair, newCombi, count)

                nextPolymerCounts[newCombi[0]] += count
                nextPolymerCounts[newCombi[1]] += count
            else:
                nextPolymerCounts[pPair] = polyCombis[pPair]

            print(nextPolymerCounts)

        polyCombiCount = nextPolymerCounts

    # dont double count chars as pairs - think about last one?
    char_count = defaultdict(int)
    for k, n in polyCombiCount.items():
        char_count[k[0]] += n

    print(char_count)

    char_count[last_char] += 1
    print(char_count)

    # for k, n in polyCombiCount.items():
    # most_freq_char = msg_char_counter.most_common()[0][0]
    # least_freq_char = msg_char_counter.most_common()[-1][0]

    answer = max(char_count.values()) - min(char_count.values())

    return answer


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    times = []

    polymer, insertion_rules = parse(puzzle_input)

    times.append(time.perf_counter())
    solution1 = part1(polymer, insertion_rules, 10)
    times.append(time.perf_counter())
    solution2 = part2(polymer, insertion_rules, 40)
    times.append(time.perf_counter())

    return solution1, solution2, times


def runTest(test_file):
    polymer, insertion_rules = parse(test_file)
    test_solution1 = part1(polymer, insertion_rules, 10)
    test_solution2 = part2(polymer, insertion_rules, 40)
    return test_solution1, test_solution2


def runAllTests():
    print("Tests")
    a, b = runTest(test_file)
    print(f"Test1.  Part1: {a} Part 2: {b}")


if __name__ == "__main__":  # print()
    runAllTests()

    solutions = solve(soln_file)
    print("\nAOC")
    print(f"Solution 1: {str(solutions[0])} in {solutions[2][1]-solutions[2][0]:.4f}s")
    print(f"Solution 2: {str(solutions[1])} in {solutions[2][2]-solutions[2][1]:.4f}s")
    print(f"\nExecution total: {solutions[2][-1]-solutions[2][0]:.4f} seconds")
