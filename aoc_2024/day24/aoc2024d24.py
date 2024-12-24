# https://adventofcode.com/2024/day/24
import pathlib
import time
import copy
from pprint import pprint as pp
from collections import defaultdict

script_path = pathlib.Path(__file__).parent
soln_file = script_path / "input.txt"  # 55920211035878 /
test_file0 = script_path / "test_0.txt"  # 4 /
test_file1 = script_path / "test_1.txt"  # 2024 /


def parse(puzzle_input):
    """Parse input"""

    with open(puzzle_input, "r", encoding="UTF-8") as file:
        #  Read each line (split \n) and form a list of strings
        parts = file.read().strip().split("\n\n")

        initial_values = {}
        for line in parts[0].splitlines():
            wire, value = line.split(": ")
            initial_values[wire] = int(value)

        wire_instructions = {}
        for line in parts[1].splitlines():
            inputs, output = line.split(" -> ")
            output = output.strip()
            gate_type = None
            if "AND" in inputs:
                gate_type = "AND"
                inputs = inputs.split(" AND ")
            elif "XOR" in inputs:
                gate_type = "XOR"
                inputs = inputs.split(" XOR ")
            elif "OR" in inputs:
                gate_type = "OR"
                inputs = inputs.split(" OR ")
            else:
                inputs = [inputs]
            wire_instructions[output] = (gate_type, inputs)

    return (initial_values, wire_instructions)


def calculate_wire_value(gate_type, input_wires, wire_values):
    """
    Calculates the value of a single wire.
    """
    if gate_type == "XOR":
        value1 = wire_values[input_wires[0]]
        value2 = wire_values[input_wires[1]]
        return int(value1) ^ int(value2)
    elif gate_type == "AND":
        value1 = wire_values[input_wires[0]]
        value2 = wire_values[input_wires[1]]
        return int(value1) & int(value2)
    elif gate_type == "OR":
        value1 = wire_values[input_wires[0]]
        value2 = wire_values[input_wires[1]]
        return int(value1) | int(value2)
    else:
        # Handle cases with single input wire (no gate)
        return wire_values[input_wires[0]]


def calculate_wire_values(initial_values, wire_instructions):
    """
    Calculates the final values of wires starting with 'z' based on the given initial values and wire instructions.

    Args:
      initial_values: A dictionary containing the initial values of some wires.
      wire_instructions: A dictionary of wire instructions,
                           where keys are output wires and values are tuples
                           containing the gate type and input wires.

    Returns:
      A dictionary containing the final values of wires starting with 'z'.
    """

    wire_values = {}
    wire_values.update(initial_values)

    # Initialize a set to keep track of gates that can be processed
    gates_to_process = set()
    for output_wire, (gate_type, input_wires) in wire_instructions.items():
        if all(wire in initial_values for wire in input_wires):
            gates_to_process.add(output_wire)

    while gates_to_process:
        current_wire = gates_to_process.pop()
        gate_type, input_wires = wire_instructions[current_wire]
        wire_values[current_wire] = calculate_wire_value(
            gate_type, input_wires, wire_values
        )

        # Add dependent gates to the set to be processed later
        for dependent_wire, (
            dependent_gate_type,
            dependent_inputs,
        ) in wire_instructions.items():
            if current_wire in dependent_inputs and all(
                wire in wire_values for wire in dependent_inputs
            ):
                gates_to_process.add(dependent_wire)

    return {wire: value for wire, value in wire_values.items() if wire.startswith("z")}


def z_values_to_decimal(z_values_dict):
    # Sort keys in ascending order (e.g., 'z00', 'z01', 'z02')
    # sorted_keys = sorted(z_values_dict.keys())
    sorted_keys = sorted(z_values_dict.keys(), key=lambda x: int(x[1:]))

    # Create a binary string
    binary_str = "".join(str(z_values_dict[key]) for key in reversed(sorted_keys))

    print(binary_str)

    # Convert binary string to decimal
    return int(binary_str, 2)


def part1(data):
    """Solve part 1"""

    start_values, wire_instructions = data

    working_wires = copy.deepcopy(wire_instructions)

    pp(start_values)
    pp(working_wires)

    ans = calculate_wire_values(start_values, working_wires)
    pp(ans)
    val = z_values_to_decimal(ans)

    return val


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

    tests = solve(test_file0, run="Test 0")
    tests = solve(test_file1, run="Test 1")

    print()
    solutions = solve(soln_file)
