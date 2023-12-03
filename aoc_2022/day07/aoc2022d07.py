# https://adventofcode.com/2022/day/7

import pathlib
import time
from collections import defaultdict
from pprint import pprint as pp
from functools import lru_cache

"""
    PROBLEMS I RAN INTO:

    Problem 1
    Python passes dictionaies are references
    When I ran the input puzzle data after tests, the test data was still in the
    dictionary, so it inflated the numbers. Lots or print steps later... realised
    
    Problems 2:
    lru_cache was screwing with part 2 answers, my code was right
    forgot about the cache for the recursion, had to to look up if could clear
    func-name.cache_clear()

"""
script_path = pathlib.Path(__file__).parent
input = script_path / "input.txt"  # 1350966 //   6296435
input_test = script_path / "test.txt"  # 95437 // 24933642

fs = defaultdict(dict)


def parse(puzzle_input):
    """Parse input"""

    with open(puzzle_input, "r") as file:
        lst = [l.split(" ") for l in file.read().replace("$ ", "$").split("\n")]

    return lst


def build_structure(data):
    current_path = tuple()

    fs.clear()

    for d in data:
        if d[0] == "$ls":
            continue

        if d[0] == "$cd":
            if d[1] == "..":
                current_path = current_path[:-1]
                continue

            current_path = current_path + (d[1],)
            continue

        if d[0] == "dir":
            tmp_dir_list = fs[current_path].get("dirs", [])
            tmp_dir_list.append(d[1])
            fs[current_path]["dirs"] = tmp_dir_list
            continue

        try:
            file_size = int(d[0])
        except:
            file_size = None

        if file_size:
            tmp_files_list = fs[current_path].get("files", [])
            tmp_files_list.append((d[1], file_size))
            fs[current_path]["files"] = tmp_files_list
            continue

    return fs


@lru_cache(maxsize=None)
def tally_directory_size(path):
    tally = 0

    for f in fs[path].get("files", []):
        tally += f[1]

    for d in fs[path].get("dirs", []):
        new_path = path + (d,)
        tally += tally_directory_size(new_path)

    return tally


def part1(data):
    """Solve part 1"""
    print("Part 1....")

    build_structure(data)
    dir_sizes = defaultdict(dict)

    for k in fs.keys():
        dir_sizes[k] = tally_directory_size(k)
    # pp(dir_sizes)

    total = 0
    valid_dirs = []
    for pth in fs:
        tmp = dir_sizes[pth]
        if tmp <= 100000:
            valid_dirs.append(pth)
            total += tmp

    # pp(valid_dirs)
    return total


def part2(data):
    """Solve part 2"""
    print("Part 2....")

    tally_directory_size.cache_clear()
    build_structure(data)
    dir_sizes = defaultdict(dict)

    for k in fs.keys():
        dir_sizes[k] = tally_directory_size(k)

    root_size = dir_sizes[("/",)]
    space_available = 70000000 - root_size
    space_required = 30000000 - space_available

    print(
        "root:",
        root_size,
        " available: ",
        space_available,
        " required: ",
        space_required,
    )

    valid_dirs = []
    for pth in fs:
        tmp = dir_sizes[pth]
        if space_required <= tmp <= root_size:
            valid_dirs.append(tmp)

    # pp(valid_dirs)

    ans = min(valid_dirs)

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
