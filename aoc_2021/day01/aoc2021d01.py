# https://adventofcode.com/2021/day/1

import pathlib

script_path = pathlib.Path(__file__).parent
input_test = script_path / 'test.txt'  # 5 
input = script_path / 'input.txt'  #  

<<<<<<< HEAD
print("Advent of Code 2021 - Day 1")

input_test = 'test.txt'  # 5 
input = 'input.txt'  #  
=======
file_in = input_test
>>>>>>> 80a36bdbe4ea494a78d875a4e5391776379c75b9


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

    # print(parse(file_in))
    # print()

    solutions = solve(file_in)

    print("Solutions")
    print("\n".join(str(solution) for solution in solutions))
