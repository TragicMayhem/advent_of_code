# https://adventofcode.com/2022/day/20

import pathlib
import time

script_path = pathlib.Path(__file__).parent
soln_file = script_path / "input.txt"  # 2622 / 1538773034088
test_file = script_path / "test.txt"  # 3 / 1623178306

DECRYPTION_KEY = 811589153


def parse(puzzle_input):
    """Parse input"""

    with open(puzzle_input, "r") as file:
        readin = list(map(int, file.read().split("\n")))

    original = []

    # now store the order each number was in the original file as a tuple
    for i, v in enumerate(readin):
        original.append((v, i))

    return original


def decrypt_code(orig, data=None):
    if data == None:
        final_seq = orig.copy()
    else:
        final_seq = data.copy()
    # print(final_seq)

    for n in orig:
        # print(">",n)
        pos = final_seq.index(n)
        v, i = pop_val = final_seq.pop(pos)
        # print(pos, pop_val, v, i)

        new_pos = (pos + v) % len(final_seq)
        # not original
        final_seq.insert(new_pos, pop_val)

        # print("new",new_pos)
        # print(final_seq)

    # print()
    # print(final_seq)
    return final_seq


def part1(data):
    """Solve part 1"""
    final_seq = decrypt_code(data)

    output = [a for a, _ in final_seq]
    print()
    # print(output)

    find_zero = output.index(0)
    # print("zero at pos", find_zero)

    n1 = output[(find_zero + 1000) % len(output)]
    n2 = output[(find_zero + 2000) % len(output)]
    n3 = output[(find_zero + 3000) % len(output)]
    ans = n1 + n2 + n3
    # print(n1, n2, n3, "ans", ans)

    return ans


def part2(data):
    """Solve part 2"""

    part2 = []

    for tup in data:
        v, i = tup
        part2.append((v * DECRYPTION_KEY, i))

    # print(part2)
    print("-" * 20)

    final_seq = part2.copy()
    for _ in range(10):
        final_seq = decrypt_code(part2, final_seq)

    output = [a for a, _ in final_seq]
    # print(output)

    find_zero = output.index(0)
    # print("zero at pos", find_zero)

    n1 = output[(find_zero + 1000) % len(output)]
    n2 = output[(find_zero + 2000) % len(output)]
    n3 = output[(find_zero + 3000) % len(output)]
    ans = n1 + n2 + n3
    # print(n1, n2, n3, "ans", ans)

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

    tests = solve(test_file, run="Test")

    print()
    solutions = solve(soln_file)
