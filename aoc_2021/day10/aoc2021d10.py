# https://adventofcode.com/2021/day/10

import pathlib
import time

script_path = pathlib.Path(__file__).parent
input = script_path / "input.txt"  # 316851 / 2182912364
input_test = script_path / "test.txt"  # 26397 / 288957


def parse(puzzle_input):
    """Parse input"""

    with open(puzzle_input, "r") as file:
        data = file.read().split("\n")
    return data


def part1(data):
    """Solve part 1"""

    # ( ) [] <>  {}
    # SCORES = {')': 3, ']': 57, '}': 1197, '>': 25137}
    # open_seq = ['(','[','{','<']
    # close_seq = [')',']','}','>']
    seq = []
    points = []

    for d in data:
        found = True
        check = d
        while found:
            if "()" in check or "[]" in check or "{}" in check or "<>" in check:
                check = (
                    check.replace("()", "")
                    .replace("[]", "")
                    .replace("{}", "")
                    .replace("<>", "")
                )
            else:
                found = False

        # add all, then filter out and then sort in one statement? how?
        closing = dict()
        if check.find(")") > 0:
            closing[")"] = check.find(")")
        if check.find("]") > 0:
            closing["]"] = check.find("]")
        if check.find("}") > 0:
            closing["}"] = check.find("}")
        if check.find(">") > 0:
            closing[">"] = check.find(">")

        lowest = None
        error_char = ""
        for k, v in closing.items():
            if lowest == None or v < lowest:
                lowest = v
                error_char = k

        if error_char == ")":
            points.append(3)
        elif error_char == "]":
            points.append(57)
        elif error_char == "}":
            points.append(1197)
        elif error_char == ">":
            points.append(25137)

    return sum(points)


def part2(data):
    """Solve part 2"""

    closing_seq = []
    scores = []

    for d in data:
        found = True
        check = d
        while found:
            if "()" in check or "[]" in check or "{}" in check or "<>" in check:
                check = (
                    check.replace("()", "")
                    .replace("[]", "")
                    .replace("{}", "")
                    .replace("<>", "")
                )
            else:
                found = False

        # add all, then filter out and then sort in one statement?
        if (
            check.find(")") > 0
            or check.find("]") > 0
            or check.find("}") > 0
            or check.find(">") > 0
        ):
            pass
        else:
            closing_seq.append(
                check.replace("(", ")")
                .replace("[", "]")
                .replace("{", "}")
                .replace("<", ">")[::-1]
            )

    for i, line in enumerate(closing_seq):
        score = 0
        for c, char in enumerate(line):
            score *= 5
            if char == ")":
                score += 1
                continue
            if char == "]":
                score += 2
                continue
            if char == "}":
                score += 3
                continue
            if char == ">":
                score += 4
                continue
        scores.append(score)

    scores.sort()
    ans = scores[int(len(scores) / 2)]

    return ans


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

    tests = solve(input_test, run="Test")

    print()
    solutions = solve(input)
