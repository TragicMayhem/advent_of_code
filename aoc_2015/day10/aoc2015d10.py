# https://adventofcode.com/2015/day/10

import pathlib
import time
from itertools import groupby

script_path = pathlib.Path(__file__).parent
input = '1113222113'  # Part 1 = 252594  // Part 2 = 3579328
input_test = '1'  # 312211 > len = 6 after 5 .... 82350 / 1166642


def solve(puzzle_input, max_count):
   
    latest_output = puzzle_input   ## Set to input string test or P
    # max_count = count   ## Set to 40 for part 1 or 50 for Part 2

    for i in range(max_count):
        new_list = list()
        grouped_content = ["".join(g) for k, g in groupby(latest_output)]
        # print("LOOP:", i, latest_output)
        # print("Grouped:", grouped_content)

        for g in grouped_content:
            new_list.append(str(len(g)) + g[0])

        latest_output = "".join(new_list)
  
    # print("\nOutput:", len(latest_output))

    return len(latest_output)


if __name__ == "__main__":    # print()

    times=[]
    
    times.append(time.perf_counter())
    ans1a = solve(input_test, 40)
    times.append(time.perf_counter())
    ans1b = solve(input_test, 50)
    times.append(time.perf_counter())
    
    print(f'Test1 Part 1: {ans1a} in {times[1]-times[0]:.4f}s')
    print(f'      Part 2: {ans1b} in {times[2]-times[1]:.4f}s')
    print(f"      Execution total: {times[-1]-times[0]:.4f} seconds")

    times=[]
    times.append(time.perf_counter())
    ans2a = solve(input, 40)
    times.append(time.perf_counter())
    ans2b = solve(input, 50)
    times.append(time.perf_counter())

    print('\nAOC')
    print(f"Solution 1: {str(ans2a)} in {times[1]-times[0]:.4f}s")
    print(f"Solution 2: {str(ans2b)} in {times[2]-times[1]:.4f}s")
    print(f"\nExecution total: {times[-1]-times[0]:.4f} seconds")