import re
import sys

print("Advent of Code 2020 - Day 2 part 1")

if sys.platform == "linux" or sys.platform == "linux2":
  dirpath = sys.path[0] + "/"
elif sys.platform == "darwin":
  dirpath = sys.path[0] + "/"
elif sys.platform == "win32":
  dirpath = sys.path[0] + "\\\\"

# Input file is a list of policy and passwords
# n-m : passwordstring
# How many on the input file are valid

valid_pwd = 0

#handle = open(dirpath + 'test.txt', 'r')
handle = open(dirpath + 'input.txt', 'r')
lines = handle.readlines()
handle.close()

for line in lines:
  # For each line use regex to group the results and store them in variables
  chk = re.match(r"(\d+)-(\d+) ([a-z]): ([a-z]+)", line)
  lower, upper, letter, password = chk.group(1, 2, 3, 4)
  # print(lower, upper, letter, password)
  lower = int(lower)
  upper = int(upper)

  # Check the password against the condition
  occurances = password.count(letter)
  if (lower <= occurances <= upper):
      valid_pwd += 1

print("Number of valid passwords is ", valid_pwd)

  


