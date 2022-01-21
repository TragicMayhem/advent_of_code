# https://adventofcode.com/2016/day/6

import pathlib
import time
from collections import Counter

script_path = pathlib.Path(__file__).parent
input = script_path / 'input.txt'       # ikerpcty  /   uwpfaqrq
input_test = script_path / 'test.txt'   # easter    /   advent


def parse(puzzle_input):
    """Parse input """
    with open(puzzle_input, 'r') as file:
        data = tuple(file.read().split('\n'))
        # print(data)
    return data


def rotate_and_count(data):

    output = [''] * len(data[0])

    for d in data:
        for i, ch in enumerate(d):
            output[i] = output[i] + ch

    counts = [item for item in (Counter(x).most_common() for x in output)]
    top_counts = [x[0] for x in counts]
    bottom_counts = [x[-1] for x in counts]

    # print('Tuple counter:\n', counts)
    # print('Top tuple from each list:\n', top_counts)
    # print('Bottom tuple from each list:\n', bottom_counts)
    
    top_seq = ''.join([str(x[0]) for x in top_counts])
    bottom_seq = ''.join([str(x[0]) for x in bottom_counts])

    return (top_seq, bottom_seq)


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    times=[]

    times.append(time.perf_counter())
    data = parse(puzzle_input)
    (solution1, solution2) = rotate_and_count(data)
    times.append(time.perf_counter())
    
    return solution1, solution2, times


def runAllTests():

    print("\nTests\n")
    a, b, t  = solve(input_test)
    print(f'Test1 Part 1: {a}')
    print(f'      Part 2: {b}')
    print(f"      Execution total: {t[-1]-t[0]:.4f} seconds")


if __name__ == "__main__":    # print()

    runAllTests()

    sol1, sol2, times = solve(input)
    print('\nAOC')
    print(f"Solution 1: {str(sol1)}")
    print(f"Solution 2: {str(sol2)}")
    print(f"\nExecution total: {times[-1]-times[0]:.4f} seconds")