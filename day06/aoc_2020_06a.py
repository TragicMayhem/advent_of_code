import sys

print("Advent of Code 2020 - Day 6 part 1")

dirpath = sys.path[0] + '\\'

# filename = 'test.txt'
filename = 'input.txt'

with open(dirpath + filename, 'r') as file:
  lst = file.read().split('\n\n')    #['abc', 'a\nb\nc', 'ab\nac', 'a\na\na\na', 'b']
  # lst = [x.replace('\n', ' ').split() for x in lst] # [['abc'], ['a', 'b', 'c'], ['ab', 'ac'], ['a', 'a', 'a', 'a'], ['b']]
  lst = [x.replace('\n', '').split() for x in lst]
  
  list_all_ans = [x for l in lst for x in l]  # Unpack lists of lists to for list of strings (answers)

  unique_lst = []
  count = 0

  for x in list_all_ans:
    tmp = set(x)
    unique_lst.append(tmp)
    count += len(tmp)

print("Total: ", count)
