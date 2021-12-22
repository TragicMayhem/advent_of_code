# https://adventofcode.com/2015/day/19

import pathlib
from sys import setprofile
import time
import copy
from pprint import pprint
import re

script_path = pathlib.Path(__file__).parent
input = script_path / 'input.txt'  # 576 / 
input_test = script_path / 'input_test.txt'  # 4 distinct in 1 replacements
input_test2 = script_path / 'input_test2.txt'  # 7 distinct in 9 replacements

# replacements = {}
# molecules = set()


def parse(puzzle_input):
  """Parse input """

  replacements = {}

  with open(puzzle_input, 'r') as file:
    data = file.read().split('\n')
    chain = data.pop(-1)

    for d in data:
      if d == '': continue
      tmp = d.split(' => ')
      if replacements.get(tmp[0], None) == None:
        replacements[tmp[0]] = []
      replacements.get(tmp[0]).append(tmp[1])

  print(chain)
  print(replacements)

  return chain, replacements    


# with open(dirpath + filename, 'r') as file:
#   data = file.read().split('\n')
#   chain = data.pop(-1)

#   for d in data:
#     if d == '': continue
#     tmp = d.split(' => ')
#     if replacements.get(tmp[0], None) == None:
#       replacements[tmp[0]] = []
#     replacements.get(tmp[0]).append(tmp[1])

#   for key, combis in replacements.items():
#     pattern = key
#     for match in re.finditer(pattern, chain):
#       s = match.start()
#       e = match.end()
#       # print( 'String match "%s" at %d:%d' % (chain[s:e], s, e))
#       for m in combis:
#         tmp_molecule = chain[:s] + m + chain[s+len(key):]
#         molecules.add(tmp_molecule)

# # print(molecules)
# print("Number of possible molecules:", len(molecules))



def part1(chain, replacements):
    """Solve part 1""" 
    molecules = set()

    for key, combis in replacements.items():
      pattern = key
      for match in re.finditer(pattern, chain):
        s = match.start()
        e = match.end()
        # print( 'String match "%s" at %d:%d' % (chain[s:e], s, e))
        for m in combis:
          tmp_molecule = chain[:s] + m + chain[s+len(key):]
          molecules.add(tmp_molecule)
     
    return len(molecules)


def part2(chain, replacements):
    """Solve part 2"""   
   
    return 1
 

def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    times=[]

    chain, replacements = parse(puzzle_input)
    
    times.append(time.perf_counter())
    solution1 = part1(chain, replacements)
    times.append(time.perf_counter())
    solution2 = part2(chain, replacements)
    times.append(time.perf_counter())
    
    return solution1, solution2, times


def runTest(test_file):
    chain, replacements = parse(test_file)
    test_solution1 = part1(chain, replacements)
    test_solution2 = part2(chain, replacements)
    return test_solution1, test_solution2


def runAllTests():
    
    print("Tests")
    a, b  = runTest(input_test)
    print(f'Test1.  Part1: {a} Part 2: {b}')
    a, b  = runTest(input_test2)
    print(f'Test2.  Part1: {a} Part 2: {b}')


if __name__ == "__main__":    # print()

    runAllTests()

    solutions = solve(input)
    print('\nAOC')
    print(f"Solution 1: {str(solutions[0])} in {solutions[2][1]-solutions[2][0]:.4f}s")
    print(f"Solution 2: {str(solutions[1])} in {solutions[2][2]-solutions[2][1]:.4f}s")
    print(f"\nExecution total: {solutions[2][-1]-solutions[2][0]:.4f} seconds")