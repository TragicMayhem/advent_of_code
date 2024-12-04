# https://adventofcode.com/2024/day/4

import pathlib
import time

script_path = pathlib.Path(__file__).parent
soln_file = script_path / "input.txt"  # 2447
test_file = script_path / "test.txt"  # 18 / 9



# Previous AOC
# def get_coords4d(r, c, h, w):
#     for delta_r, delta_c in ((-1, 0), (1, 0), (0, -1), (0, 1)):
#         rr, cc = (r + delta_r, c + delta_c)
#         if 0 <= rr < h and 0 <= cc < w:
#             yield (rr, cc)

# Previous AOC
# def get_coords8d(r, c, h, w):
#     for delta_r, delta_c in (
#         (-1, 0),
#         (1, 0),
#         (0, -1),
#         (0, 1),
#         (-1, -1),
#         (-1, 1),
#         (1, -1),
#         (1, 1),
#     ):
#         rr, cc = (r + delta_r, c + delta_c)
#         if 0 <= rr < h and 0 <= cc < w:
#             yield (rr, cc)


# new
def get_deltas_8d():
    deltas = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1),
        (-1, -1),
        (-1, 1),
        (1, -1),
        (1, 1),
    ]

    for (r,c) in deltas:
        yield (r,c)


# new
def get_deltas_4diag():
    deltas = [
        (-1, -1),
        (-1, 1),
        (1, -1),
        (1, 1),
    ]

    for (r,c) in deltas:
        yield (r,c)



def check_for_xmas(data, start_r, start_c, delta_r, delta_c):  
    # Take first letter, then do the check 3 more times
    word = ''

    for cnt in range(4): # 0123

        new_deltar = delta_r * cnt
        new_deltac = delta_c * cnt
        rr = start_r + new_deltar
        cc = start_c + new_deltac

        if 0 <= rr < len(data[0]) and 0 <= cc < len(data):
            word += data[rr][cc]
        else:
            break

    # if word == 'XMAS':
    #     print(start_r, start_c, delta_r, delta_c, word)

    return word

def validate_coords(r, c, data):
    if 0 <= r < len(data[0]) and 0 <= c < len(data):
        return data[r][c]
    return ""


def check_for_mas(data, start_r, start_c):
    diag_1 = [(-1, -1),(0, 0),(1, 1)]
    diag_2 = [(1, -1),(0, 0),(-1, 1)]

    valid = ["MAS", "SAM"]

    way1 = way2 = ""

    for delta_r, delta_c in diag_1:
        way1 += validate_coords(start_r + delta_r, start_c + delta_c, data)

    for delta_r, delta_c in diag_2:
        way2 += validate_coords(start_r + delta_r, start_c + delta_c, data)

    # print(way1,way2)

    return way1 in valid and way2 in valid


def parse(puzzle_input):
    """Parse input"""

    with open(puzzle_input, "r", encoding="UTF-8") as file:
        #  Read each line (split \n) and form a list of strings
        lst = [[x for x in row] for row in file.read().split("\n")]

    # print(lst)

    return lst


def part1(data):
    """Solve part 1"""

    h = len(data)
    w = len(data[0])

    word_count = 0

    # 8 directions, 4 letter word, so need to go from character out 8 directions 4 times
    for r in range(w):
        for c in range(h):
            # print(r, c, data[r][c])

            for delta_r, delta_c in get_deltas_8d():
                tmp_word = check_for_xmas(data, r, c, delta_r, delta_c)

                if tmp_word == 'XMAS':
                    word_count += 1

    # print(word_count)

    return word_count


def part2(data):
    """Solve part 2"""

    h = len(data)
    w = len(data[0])
    count = 0

    for r in range(w):
        for c in range(h):
            if check_for_mas(data, r, c):
                count += 1

    return count


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

    print()
    solutions = solve(soln_file)
