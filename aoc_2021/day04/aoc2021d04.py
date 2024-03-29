# https://adventofcode.com/2021/day/4

import pathlib
import time

script_path = pathlib.Path(__file__).parent
soln_file = script_path / "input.txt"  #  39984 / 8468
test_file = script_path / "test.txt"  # 4512 / 1924
test_file2 = script_path / "test2.txt"  # 2607 - testing column win pt1 / 2192


def make_grids(data):
    output = []
    tmp = []

    for i, d in enumerate(data):
        if i == 0:
            continue
        if d == []:
            output.append(tmp)
            tmp = []
            continue
        tmp.append(d)

    output.append(tmp)
    return output


def search_and_mark(source, item):
    for i in range(len(source)):
        if source[i] == item:
            source[i] = source[i] + "x"
            return True
    return False


def check_win(grid):
    for row in grid:
        win_row = "".join(row).count("x") == 5
        if win_row:
            break

    cols = list(zip(*grid))
    for col in cols:
        win_col = "".join(col).count("x") == 5
        if win_col:
            break

    return win_col or win_row


def parse(puzzle_input):
    """Parse input"""

    with open(puzzle_input, "r") as file:
        input_data = [line.split() for line in file]

        ball_list = [ball for line in input_data[0] for ball in line.split(",")]
        del input_data[0]

    return ball_list, input_data


def part1(balls, data):
    """Solve part 1"""

    grids = make_grids(data)

    checked = []
    winning_grid_id = 0
    last_ball = 0

    for b in balls:
        checked.append(b)
        # print('\n<<<<< BALL >>>>>>>', b)

        for i in range(len(grids)):
            for row in grids[i]:
                search_and_mark(row, b)

            win_status = check_win(grids[i])
            if win_status:
                break

        if win_status:
            winning_grid_id = i
            last_ball = int(b)
            break

    # print('------------------')
    # print('grid', winning_grid_id, 'ball', last_ball)
    # print(grids[winning_grid_id])

    running_total = 0

    for i, row in enumerate(grids[winning_grid_id]):
        for j in row:
            if "x" in j:
                continue
            else:
                running_total += int(j)

    return running_total * last_ball


def part2(balls, data):
    """Solve part 2"""
    grids = make_grids(data)

    checked = []
    winning_grid_id = 0
    last_ball = 0

    win_grid_ids = []
    win_combis = []

    while len(balls) > 0 and len(grids) > len(win_grid_ids):
        b = balls.pop(0)
        checked.append(b)

        # print('\n<<<<< BALL >>>>>>>', b, 'WC', win_combis, '/', win_grid_ids)

        for i in range(len(grids)):
            if i not in win_grid_ids:
                for row in grids[i]:
                    search_and_mark(row, b)
                win_status = check_win(grids[i])

                if win_status:
                    win_grid_ids.append(i)
                    win_combis.append([i, int(b)])
                    last_ball = int(b)

    winning_grid_id = win_grid_ids[-1]
    # print('------------------')
    # print('grid', winning_grid_id, 'ball', last_ball)
    # print(grids[winning_grid_id])

    running_total = 0

    for i, row in enumerate(grids[winning_grid_id]):
        for j in row:
            if "x" in j:
                continue
            else:
                running_total += int(j)

    return running_total * last_ball


def solve(puzzle_input, run="Solution"):
    """Solve the puzzle for the given input"""
    times = []

    balls, data = parse(puzzle_input)

    times.append(time.perf_counter())
    solution1 = part1(balls, data)
    times.append(time.perf_counter())
    solution2 = part2(balls, data)
    times.append(time.perf_counter())

    print(f"{run} 1: {str(solution1)} in {times[1]-times[0]:.4f}s")
    print(f"{run} 2: {str(solution2)} in {times[2]-times[1]:.4f}s")
    print(f"\nExecution total: {times[-1]-times[0]:.4f} seconds")

    return solution1, solution2, times


if __name__ == "__main__":
    print("\nAOC")

    tests = solve(test_file, run="Test")
    tests2 = solve(test_file2, run="Test 2")

    print()
    solutions = solve(soln_file)
