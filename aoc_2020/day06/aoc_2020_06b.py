import sys
from pprint import pprint

print("Advent of Code 2020 - Day 6 part 2")

dirpath = sys.path[0] + '\\'

filename = 'test.txt'
# filename = 'input.txt'

with open(dirpath + filename, 'r') as file:
  # Split on double new line to create groups. replace \n with '' then split all strings into a list. 
  lst = file.read().split('\n\n')    #['abc', 'a\nb\nc', 'ab\nac', 'a\na\na\na', 'b']
  lst = [x.replace('\n', ' ').split() for x in lst]
  pprint(lst)

  count = 0

  for a in lst:
    how_many_in_group = len(a)  # Count how many responses in total in current list
    all_answers = ''.join(a)  # Join all the answers together into one string
    unique_ans = set(all_answers)  # Set this string to get the unique answers
    
    # Read through each unique answer, if the all answers count has the same number as the total responses thats all answered same.
    for x in unique_ans:
      if all_answers.count(x) == how_many_in_group:
        # print("group answered yes to same question +1")
        count += 1

print("Total: ", count)
