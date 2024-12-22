#
#  https://adventofcode.com/2024/day/22

import pathlib
import time

script_path = pathlib.Path(__file__).parent
soln_file = script_path / "input.txt"  #
test_file = script_path / "test.txt"  # 37327623


def parse(puzzle_input):
    """Parse input"""

    with open(puzzle_input, "r", encoding="UTF-8") as file:
        #  Read each line (split \n) and form a list of strings
        lst = file.read().split("\n\n")

    return lst


def bitwise_xor(x, y):
    """
    Calculates the bitwise XOR of two numbers.

    Args:
      x: The first number.
      y: The second number.

    Returns:
      The result of the bitwise XOR operation.
    """
    return x ^ y


def modulo_16777216(number):
    """
    Calculates the modulo 16777216 of a given number.

    Args:
      number: The input number.

    Returns:
      The result of the number modulo 16777216.
    """
    return number % 16777216


# Example usage:
# num1 = 42
# num2 = 15
# result = bitwise_xor(num1, num2)
# print(f"The bitwise XOR of {num1} and {num2} is: {result}")

# num = 100000000
# result = modulo_16777216(num)
# print(f"The result of {num} modulo 16777216 is: {result}")


def first_step(number):
    """
    Performs the first step of the sequence:
      1. Multiply by 64.
      2. Bitwise XOR with the original number.
      3. Modulo 16777216.

    Args:
      number: The input number.

    Returns:
      The result of the first step.
    """
    return (number * 64) ^ number % 16777216


def second_step(number):
    """
    Performs the second step of the sequence:
      1. Divide by 32 and round down.
      2. Bitwise XOR with the original number.
      3. Modulo 16777216.

    Args:
      number: The input number.

    Returns:
      The result of the second step.
    """
    return (number // 32) ^ number % 16777216


def third_step(number):
    """
    Performs the third step of the sequence:
      1. Multiply by 2048.
      2. Bitwise XOR with the original number.
      3. Modulo 16777216.

    Args:
      number: The input number.

    Returns:
      The result of the third step.
    """
    return (number * 2048) ^ number % 16777216


# Example usage:
example_number = 123
result = first_step(example_number)
result = second_step(result)
result = third_step(result)
print(f"Result of chaining for {example_number}: {result}")


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
seed_number = 123
iterations = 10

result = generate_sequence(seed_number, iterations)
print(f"The final number in the sequence is: {result}")  # Output: 15887950

# CANT DO, DOESNT TAKE INTO ACCOUNT THE ROUNDING DOWN
# def generate_sequence_simplified(seed_number, iterations):
#     """
#     Generates the sequence of numbers based on the given seed number and iterations.

#     Args:
#         seed_number: The starting number for the sequence.
#         iterations: The number of times to loop and generate the sequence.

#     Returns:
#         The final number in the sequence.
#     """

#     current_number = seed_number

#     for _ in range(iterations):
#         current_number = (current_number * 4096) % 16777216

#     return current_number


# Example usage v1:
seed_number = 123
iterations = 10

result = generate_sequence(seed_number, iterations)
print(f"The final number in the sequence is: {result}")  # Output: 15887950


def part1(data):
    """Solve part 1"""

    return 1


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
