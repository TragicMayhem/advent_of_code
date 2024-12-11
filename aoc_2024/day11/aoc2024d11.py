# https://adventofcode.com/2024/day/11

import pathlib
import time
from collections import deque
from functools import lru_cache, cache

script_path = pathlib.Path(__file__).parent
soln_file = script_path / "input.txt"  # 188902 /
test_file = script_path / "test.txt"  # 55312 /

# 65601038650482 Too Low

def parse(puzzle_input):
    """Parse input"""

    with open(puzzle_input, "r", encoding="UTF-8") as file:
        #  Read each line (split \n) and form a list of strings
        lst = [int(x) for x in file.read().split()]

    return lst

## Doesnt run with 75 iterations.....
def process_queue(queue):
    new_queue = deque()
    while queue:
        num = queue.popleft()
        if len(str(num)) % 2 == 0:
            # Split even-digit number
            mid = len(str(num)) // 2
            left, right = int(str(num)[:mid]), int(str(num)[mid:])
            new_queue.extend([left, right])
        else:
            # Process odd-digit number
            new_queue.append(num * 2024 if num != 0 else 1)

    return new_queue


def run_scenario(q, n=25):
    queue = deque(q)
    count = 0

    while count < n:
        #print(count)
        queue = process_queue(queue)
        count+= 1

    return len(queue)


## Doesnt run with 75 iterations.....
def process_queue2(queue):
    new_queue = deque()
    while queue:
        num = queue.popleft()
        if num == 0:
            new_queue.append(1)
        else:
            digits = 0
            temp = num
            while temp > 0:
                digits += 1
                temp //= 10

            if digits % 2 == 0:
                divisor = 10 ** (digits // 2)
                left, right = num // divisor, num % divisor
                new_queue.extend([left, right])
            else:
                new_queue.append(num * 2024)

    return new_queue


def process_queue2(queue):
    new_queue = deque()
    while queue:
        num = queue.popleft()
        if num == 0:
            new_queue.append(1)
        else:
            digits = 0
            temp = num
            while temp > 0:
                digits += 1
                temp //= 10

            if digits % 2 == 0:
                divisor = 10 ** (digits // 2)
                left, right = num // divisor, num % divisor
                new_queue.extend([left, right])
            else:
                new_queue.append(num * 2024)

    return new_queue


def run_scenario2(q, n=25):
    queue = deque(q)
    count = 0

    while count < n:
        #print(count)
        queue = process_queue2(queue)
        count+= 1

    return len(queue)


# LRUCACHE
# Had to look up how it works again and the demo of fgibonacci

# Key is the process the numbers so that pattern is repeated,
# and the caching can speed up the process.

# reading this, you need something to identify a cycle, thats unique
# arguments must be hashable, so unique for the lifttime as its
# using a dictionary to store and recall.

# I could not work out what would the hashable bit be, so had to use
# slack thread for team pointers and some number examples from the www

# Dont need my own dictionary - well I cant get it to work with a loop
# so lru_cache creates the dictionar as long as the arguments make it
# hashable

# @lru_cache(max_size=None)
@cache
def process_stones(stone, blinks):

    # No more blinks return 1
    if blinks == 0:
        return 1

    # Rule 1
    # The base case, from advice for part 2, this is repeatable
    # pattern 0 > 1 > 2024 > 20 24 > 2 0 2 4  
    if stone == 0 :
        return process_stones(1, blinks - 1)

    digits = 0
    temp = stone
    while temp > 0:
        digits += 1
        temp //= 10

    if digits % 2 == 0:
        divisor = 10 ** (digits // 2)
        left = process_stones( stone // divisor, blinks - 1)
        right = process_stones( stone % divisor, blinks - 1)
        return left + right

    return process_stones( stone * 2024, blinks - 1)


def part1(data):
    """Solve part 1"""
    return run_scenario2(data)


def part2(data):
    """Solve part 2"""

    # Run part 1 as a test
    print("Should return same as part 1 answer")
    res = 0
    for d in data:
        res += process_stones(d, 25)
    print("LRU Blink 25", res)

    print()
    res = 0
    for d in data:
        print(d)
        res += process_stones(d, 75)


    return res


def solve(puzzle_input, run="Solution"):
    """Solve the puzzle for the given input"""
    times = []

    data = parse(puzzle_input)

    print("TESTS")
    nums = [1234, 567, 890, 1, 0]
    print(run_scenario(nums))
    print(run_scenario2(nums))

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
    # solutions = solve(soln_file)
