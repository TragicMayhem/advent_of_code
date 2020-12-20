import re

print("Advent of Code 2020 - Day 3 part 1")

# Input pattern of trees(#) and space(.)
# This repeats to the the right indefinately
# Going right 3, down 1 - how many trees would encounter?

handle = open('test.txt', 'r')
#handle = open('input.txt', 'r')
lines = handle.readlines()
handle.close()


