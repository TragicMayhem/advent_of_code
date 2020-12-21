import re
import sys

print("Advent of Code 2020 - Day 3 part 1")

dirpath = sys.path[0] + '\\'
# Input pattern of trees(#) and space(.)
# This repeats to the the right indefinately
# Going right 3, down 1 - how many trees would encounter?

handle = open(dirpath + 'test.txt', 'r')
#handle = open(dirpath + 'input.txt', 'r')
lines = handle.readlines()
handle.close()

count_trees = 0
pos_x = 0
pos_y = 0
length_of_line = len(lines(0))

print(length_of_line)

for i in range(len(lines)):


#   for j in lines_list(i):