#
#  https://adventofcode.com/2024/day/22

import pathlib
import time

script_path = pathlib.Path(__file__).parent
soln_file = script_path / "input.txt"  # 20411980517
test_file = script_path / "test.txt"  # 37327623


def parse(puzzle_input):
    """Parse input"""

    with open(puzzle_input, "r", encoding="UTF-8") as file:
        #  Read each line (split \n) and form a list of strings
        lst = [int(line.strip()) for line in file]

    return lst


def generate_sequence(seed_number, iterations):
    """
    Generates a sequence of numbers based on the given seed number and iterations.

    Args:
        seed_number: The starting number for the sequence.
        iterations: The number of times to loop and generate the sequence.

    Returns:
        The final number in the sequence.
    """

    current_number = seed_number

    for _ in range(iterations):
        # Step 1: Multiply by 64, XOR with itself, modulo 16777216
        current_number = ((current_number * 64) ^ current_number) % 16777216

        # Step 2: Divide by 32, round down, XOR with itself, modulo 16777216
        current_number = ((current_number // 32) ^ current_number) % 16777216

        # Step 3: Multiply by 2048, XOR with itself, modulo 16777216
        current_number = ((current_number * 2048) ^ current_number) % 16777216

    return current_number


# Example usage:
# seed_number = 123
# iterations = 10

# result = generate_sequence(seed_number, iterations)
# print(f"The final number in the sequence is: {result}")  # Output: 15887950

# CANT DO 4096 simplifed, DOESNT TAKE INTO ACCOUNT THE ROUNDING DOWN
#         current_number = (current_number * 4096) % 16777216


def part1(data):
    """Solve part 1"""

    res = 0
    for d in data:
        res += generate_sequence(d, 2000)

    return res


def part2(data):
    """Solve part 2"""

    return 1


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
