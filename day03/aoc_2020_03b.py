import re
import sys

print("Advent of Code 2020 - Day 3 part 2")

dirpath = sys.path[0] + '\\'

# Input pattern of trees(#) and space(.)
# This repeats to the the right indefinately
# Going right 3, down 1 - how many trees would encounter?

# handle = open(dirpath + 'test.txt', 'r')
handle = open(dirpath + 'input.txt', 'r')
lines = handle.readlines()
handle.close()

for i in range(len(lines)):
  lines[i] = lines[i].rstrip()

# (Right, down)
variations = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
tree_counts = []
answer = 1
tree = "#"
pattern_width = len(lines[0].rstrip()) - 1

for var in variations:
  count_trees = 0
  pos_x = 0
  move_x, move_y = var

  for pos_y in range(len(lines)): 

    if pos_y % move_y > 0:
      continue

    if pos_y > 0 and lines[pos_y][pos_x] == tree:
      count_trees += 1      
    
    pos_x += move_x
    
    if pos_x > pattern_width:
      pos_x = pos_x - pattern_width - 1
  
  tree_counts.append(count_trees)
  answer *= count_trees

print("Tree counts: ", tree_counts, " final answer: ", answer)

