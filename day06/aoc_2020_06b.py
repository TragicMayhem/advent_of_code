import sys

print("Advent of Code 2020 - Day 6 part 2")

dirpath = sys.path[0] + '\\'

# filename = 'test.txt'
filename = 'input.txt'

with open(dirpath + filename, 'r') as file:
  lst = file.read().split('\n\n')    #['abc', 'a\nb\nc', 'ab\nac', 'a\na\na\na', 'b']
  lst = [x.replace('\n', ' ').split() for x in lst]
    
  count = 0

  for a in lst:
    how_many_in_group = len(a)
    all_answers = ''.join(a)
    unique_ans = set(all_answers)
    
    for x in unique_ans:
      if all_answers.count(x) == how_many_in_group:
        # print("group answered yes to same question +1")
        count += 1

print("Total: ", count)
