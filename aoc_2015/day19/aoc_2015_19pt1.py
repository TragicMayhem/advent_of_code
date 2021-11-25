import sys
import re
from pprint import pprint

# https://adventofcode.com/2015/day/19

print("Advent of Code 2015 - Day 19 part 1")
if sys.platform == "linux" or sys.platform == "linux2":
  dirpath = sys.path[0] + "/"
elif sys.platform == "darwin":
  dirpath = sys.path[0] + "/"
elif sys.platform == "win32":
  dirpath = sys.path[0] + "\\\\"


# filename = 'test1.txt'  # 4 distinct in 1 replacements
# filename = 'test2.txt'  # 7 distinct in 9 replacements
filename = 'input.txt' # 576

replacements = {}
molecules = set()

with open(dirpath + filename, 'r') as file:
  data = file.read().split('\n')
  chain = data.pop(-1)

  for d in data:
    if d == '': continue
    tmp = d.split(' => ')
    if replacements.get(tmp[0], None) == None:
      replacements[tmp[0]] = []
    replacements.get(tmp[0]).append(tmp[1])

  for key, combis in replacements.items():
    pattern = key
    for match in re.finditer(pattern, chain):
      s = match.start()
      e = match.end()
      # print( 'String match "%s" at %d:%d' % (chain[s:e], s, e))
      for m in combis:
        tmp_molecule = chain[:s] + m + chain[s+len(key):]
        molecules.add(tmp_molecule)

# print(molecules)
print("Number of possible molecules:", len(molecules))