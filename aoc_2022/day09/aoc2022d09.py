# https://adventofcode.com/2022/day/9

import pathlib
import time
from pprint import pprint as pp

script_path = pathlib.Path(__file__).parent
input = script_path / "input.txt"  # 6494 // 2691
input_test = script_path / "test.txt"  # 13 // 1
input_test2 = script_path / "test2.txt"  # ?88? Not proved // 36


# Previous AOC
def get_cardinals(r, c, h, w):
    for delta_r, delta_c in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        rr, cc = (r + delta_r, c + delta_c)
        if 0 <= rr < h and 0 <= cc < w:
            yield (rr, cc)


# TO DO - use this coord = tuple(sum(x) for x in zip(coord, change)


def get_surrounding(r, c, h, w):
    for delta_r, delta_c in (
        (-1, 1),
        (-1, 0),
        (-1, -1),
        (0, 1),
        (0, 0),
        (0, -1),
        (1, 1),
        (1, 0),
        (1, -1),
    ):
        rr, cc = (r + delta_r, c + delta_c)
        yield (rr, cc)

        # if 0 <= rr < h and 0 <= cc < w:
        # yield (rr, cc)


def parse(puzzle_input):
    """Parse input"""

    trans_dict = {"L": "-1,0", "R": "1,0", "U": "0,1", "D": "0,-1"}
    table = str.maketrans(trans_dict)

    with open(puzzle_input, "r", encoding="utf-8") as file:
        lst = file.read().translate(table).split("\n")

    data = []
    for line in lst:
        a, b = line.split()
        tmp = a.split(",")
        a = (int(tmp[0]), int(tmp[1]))
        b = int(b)
        data.append((a, b))
    return data


def part1(data):
    """Solve part 1"""
    head_pos = (0, 0)
    tail_pos = (0, 0)

    visitedList = [tail_pos]

    for d_tup, qty in data:
        for _ in range(1, qty + 1):
            new_x = head_pos[0] + d_tup[0]
            new_y = head_pos[1] + d_tup[1]
            head_pos = (new_x, new_y)
            checkTailPos = tail_pos in get_surrounding(*head_pos, 100, 100)

            # In range, move on
            if checkTailPos:
                continue

            x_diff = head_pos[0] - tail_pos[0]
            y_diff = head_pos[1] - tail_pos[1]

            dx = 1 if x_diff > 0 else -1 if x_diff < 0 else 0
            dy = 1 if y_diff > 0 else -1 if y_diff < 0 else 0

            tail_pos = (
                tail_pos[0] + dx,
                tail_pos[1] + dy,
            )

            visitedList.append(tail_pos)

    ans = len(set(visitedList))
    print("\nEND: H ", head_pos, " T ", tail_pos, " visiting ", ans, " unique points")

    return ans


def part2(data):
    """Solve part 2"""

    # need a list of the points h to t
    # work along the linst, change one, then check that one against the one before.
    # iterate through the list

    knots = [
        (0, 0),
        (0, 0),
        (0, 0),
        (0, 0),
        (0, 0),
        (0, 0),
        (0, 0),
        (0, 0),
        (0, 0),
        (0, 0),
    ]

    visitedList = [knots[9]]

    # Loop the moves for the head knot - knots[0]
    for d_tup, qty in data:
        # print("\nNEXT: ", d_tup, qty)

        for _ in range(1, qty + 1):
            # HEAD moves, rest follows
            new_x = knots[0][0] + d_tup[0]
            new_y = knots[0][1] + d_tup[1]
            knots[0] = (new_x, new_y)

            # Loop through remaining knots and replace
            for k in range(1, len(knots[1:]) + 1):
                checkKnotPos = knots[k] in get_surrounding(*knots[k - 1], 100, 100)

                # In range, move on
                if checkKnotPos:
                    continue

                x_diff = knots[k - 1][0] - knots[k][0]
                y_diff = knots[k - 1][1] - knots[k][1]

                dx = 1 if x_diff > 0 else -1 if x_diff < 0 else 0
                dy = 1 if y_diff > 0 else -1 if y_diff < 0 else 0

                knots[k] = (
                    knots[k][0] + dx,
                    knots[k][1] + dy,
                )

            visitedList.append(knots[9])

    ans = len(set(visitedList))

    print(
        "\nEND: knots[0] ",
        knots[k],
        " knots[9] ",
        knots[9],
        " visiting ",
        ans,
        " unique points",
    )

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
    # tests2 = solve(input_test2, run="Test2")

    print()
    solutions = solve(input)
