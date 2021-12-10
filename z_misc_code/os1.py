import os
import sys

print("\nOS test")

print(os.path.dirname(os.path.realpath(__file__)))

fullpath_name = os.path.realpath(__file__)
print(fullpath_name)

dirpath = os.path.dirname(fullpath_name)
print(dirpath)

print("\nsys test")

print(sys.path[0])