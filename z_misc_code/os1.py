import os
import sys
from sys import platform

print("\nOS test")

print(os.path.dirname(os.path.realpath(__file__)))

fullpath_name = os.path.realpath(__file__)
print(fullpath_name)

dirpath = os.path.dirname(fullpath_name)
print(dirpath)

print("\nsys test")

print(sys.path[0])

if platform == "linux" or platform == "linux2":
    print("linux")   
elif platform == "darwin":
    print("OS X")  
elif platform == "win32":
    print("Windows")