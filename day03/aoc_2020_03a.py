import sys

print("Advent of Code 2020 - Day 3 part 1")

dirpath = sys.path[0] + '\\'

# Input pattern of trees(#) and space(.)
# This repeats to the the right indefinately
# Going right 3, down 1 - how many trees would encounter?

# handle = open(dirpath + 'test.txt', 'r')
handle = open(dirpath + 'input.txt', 'r')
lines = handle.readlines()
handle.close()

tree = "#"
count_trees = 0
pos_x = 0
pattern_width = len(lines[0].rstrip()) - 1

for pos_y in range(len(lines)):
  lines[pos_y] = lines[pos_y].rstrip()

  if pos_y > 0 and lines[pos_y][pos_x] == tree:
    count_trees += 1      

  pos_x += 3

  if pos_x > pattern_width:
    pos_x = pos_x - pattern_width - 1

print("Number of trees:", count_trees)