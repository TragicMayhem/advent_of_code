import sys
import copy
from pprint import pprint

print("Advent of Code 2020 - Day 8 part 2")

dirpath = sys.path[0] + '\\'

# filename = 'test.txt'
filename = 'input.txt'


with open(dirpath + filename, 'r') as file:
  lst = file.read().split('\n')
  lst = [x.split() for x in lst]
  lst = [[x[0], int(x[1])] for x in lst]

  # pprint(lst)

  accumulator = 0
  candidates_to_change = [] 

  for i, x in enumerate(lst):
    if x[0] == 'nop' or x[0] == 'jmp':
      candidates_to_change.append([x[0], i])

  # print("\ncandidates_to_change")
  # pprint(candidates_to_change)

  def check_soln(data_copy):
    pnt = acc = 0
    v = [] 

    while (pnt not in v) and (pnt < len(data_copy)):
      v.append(pnt)
    
      if data_copy[pnt][0] == 'nop':
        pnt += 1

      elif data_copy[pnt][0] == 'jmp':
        pnt += data_copy[pnt][1]

      elif data_copy[pnt][0] == 'acc':    
        acc += data_copy[pnt][1]
        pnt += 1

      # print("  pointer is now", pnt, "already visited", len(v), "accumulator =", acc)

    if pnt == len(data_copy):
      return (True, acc)
    
    return (False, acc)    


  for i, x in enumerate(candidates_to_change):   
    working_copy = copy.deepcopy(lst)
    
    if x[0] == 'nop':
      working_copy[x[1]][0] = 'jmp'
    else:
      working_copy[x[1]][0] = 'nop'
    
    status, accumulator = check_soln(working_copy)

    print("Changing", x, "the solution status =", status, " with accumulator =", accumulator)
    
    if status:
      break
    
print("\nFinal solution status =", status, "with accumulator =", accumulator)
