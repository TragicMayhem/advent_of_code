# Code from Python in 75 minutes
# https://www.youtube.com/watch?v=VchuKL44s6E

# some basics
# types, arithmetic, if then else, for loop, while look
# output printing
# user input
# files
# dir and help
# functions
# standard libraries and uses
# lists, tuples, sets, dictionaries
# comprehension
# Functions
# *args & **kwargs
# Scope & Globals
# Exceptions
# Handling Exceptions
# Lambda
# Map and Filter
# F Strings
# menu to play
# function to pad string when printing out



x = [0, 1, 2, 3, 4, 5]
print("List x =", x)

x.extend([44, 55, 66, 77])  # Extend list with new list and print
y = x  # Same list just a POINTER reference to the objects. Changes to X affect y
y_copy = x[:]  # This takes a copy of the list. They are now separate

print("\nx.extend([44, 55, 66, 77]) = ", x)
print('x.pop()  = ', x.pop())  # Takes off the last element (returns it so changes x)
print('x        = ', x)  # x has one less number
print('y        = ', y)  # y ALSO has one less number
print('y_copy   = ', y_copy)  # However y_copy is the same as athe original list
print('x.pop(5) = ', x.pop(5))  # This pops (returns) and specific index from the list
print('x        = ', x)  # list x now has idex 5 missing

print("\nLoop: Print 0 up to 10 (not including 10)")
for i in range(10):
    print(i, end=' ')

print("\nLoop: Print 10 down to 0")
for i in range(10, -1, -1):
    print(i, end=' ')

print("\nIterating through elements in a list")
print("(means go through all the elements in the list)")
for i in x:
    print(i, end=' ')

print("\nAn alternate way of printing out the elements of x")
for i in range(len(x)):
    print(x[i], end=' ')

# Experimenting with concatenating strings
print("")
temp_output = ""
for i, element in enumerate(x):
    temp_output += "(" + str(i) + "," + str(element) + ") "
    # If you use sep="", end=',' then it adds final comma to the end
    # print("(", i, ",", element,") ", sep="", end=',')

print("output = ", temp_output)


print("\n\nSlicing: variable[start:stop:step]")
test_word = "Learn Python"
test_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Slicing works with lists and tuples....")
print("Starting Variable.", test_list)
print("test_list[:4].....", test_list[:4])  # Beginning up to 4 (not including)
print("test_list[3:].....", test_list[3:])  # From 3 to the end
print("test_list[1:5]....", test_list[1:5])  # From 1 up to 5 (not including)
print("test_list[0:5:2]..", test_list[0:5:2])  # From 0 (don't need to include really) up to 5 step of 2
print("test_list[6:2:-1].", test_list[6:2:-1])  # Step backwards from 6 down to 2
print("test_list[::-1]...", test_list[::-1])  # This REVERSES the list


print("\nSlicing works with strings....")
print("Starting Variable.", test_word)
print("test_word[:4].....", test_word[:4])  # Beginning up to 4 (not including)
print("test_word[3:].....", test_word[3:])  # From 3 to the end
print("test_word[1:5]....", test_word[1:5])  # From 1 up to 5 (not including)
print("test_word[0:5:2]..", test_word[0:5:2])  # From 0 (don't need to include really) up to 5 step of 2
print("test_word[6:2:-1].", test_word[6:2:-1])  # Step backwards from 6 down to 2
print("test_word[::-1]...", test_word[::-1])  # This REVERSES the list

