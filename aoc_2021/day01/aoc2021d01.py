# https://adventofcode.com/2021/day/1

import sys

if sys.platform == "linux" or sys.platform == "linux2":
  dirpath = sys.path[0] + "/"
elif sys.platform == "darwin":
  dirpath = sys.path[0] + "/"
elif sys.platform == "win32":
  dirpath = sys.path[0] + "\\\\"

print("Advent of Code 2021 - Day 1b")

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

    with open(dirpath + filename, 'r') as file:
      lst = file.read().split('\n')   #  Read each line (split \n) and form a list of strings
      lst = [int(n) for n in lst]

      for x in lst[1:]:
        total = total +1 if (x > prev) else total 
        prev = x
      
    print("Total increase is", total)  


def part2(data):
    """Solve part 2"""   

    total = 0
    prev = 0

    with open(dirpath + filename, 'r') as file:
      lst = file.read().split('\n')   #  Read each line (split \n) and form a list of strings
      lst = [int(n) for n in lst]

      for i, x in enumerate(lst[:-3]):
        next = sum(lst[i:i+3])
        total = total + 1 if (next > prev) else total
        prev = next

    print("Total increase is", total)  


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    print ('main')
    puzzle_input = dirpath + filename
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
