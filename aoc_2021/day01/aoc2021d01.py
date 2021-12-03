# https://adventofcode.com/2021/day/1


import pathlib
import sys

script_path = pathlib.Path(__file__).parent

if sys.platform == "linux" or sys.platform == "linux2":
  dirpath = sys.path[0] + "/"
elif sys.platform == "darwin":
  dirpath = sys.path[0] + "/"
elif sys.platform == "win32":
  dirpath = sys.path[0] + "\\\\"

print("Advent of Code 2021 - Day 1")

input_test = 'test.txt'  # 5 
input = 'input.txt'  #  


def parse(puzzle_input):
    """Parse input"""

    with open(puzzle_input, 'r') as file:
      lst = file.read().split('\n')   #  Read each line (split \n) and form a list of strings

    return [int(n) for n in lst]



def part1(data):
    """Solve part 1""" 

    total = 0
    prev = 0
    for x in data[1:]:
      total = total +1 if (x > prev) else total 
      prev = x
      
    return total


def part2(data):
    """Solve part 2"""   

    total = 0
    prev = 0

    for i, x in enumerate(data[:-3]):
      next = sum(data[i:i+3])
      total = total + 1 if (next > prev) else total
      prev = next

    return total
 

def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    print ('main')

    in_file_1 = pathlib.Path.cwd() / "in" / "input.xlsx"
    out_file_1 = pathlib.Path.cwd() / "out" / "output.xlsx"
    parts = ["in", "input.xlsx"]
    in_file_3 = pathlib.Path.cwd().joinpath(*parts)

    print(in_file_1)
    print(type(in_file_1))
    
    print('__file__:    ', __file__)

    print(script_path)
    print(pathlib.Path.cwd())
    # file_in = pathlib.Path.cwd() / "aoc_2021" / "day01" / "input_test.txt"
    # file_in = script_path / "input.txt"
    file_in = script_path / "input_test.txt"
    print(file_in)
    puzzle_input = pathlib.Path(file_in).read_text().strip()
    print(puzzle_input)
    print()

    print(parse(file_in))

    solutions = solve(file_in)

    print("\n".join(str(solution) for solution in solutions))
