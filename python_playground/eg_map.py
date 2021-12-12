

def square(x):
  return x*x

# The map() function calls the specified function for each item of an iterable 
# (such as string, list, tuple or dictionary) and returns a list of results.

numbers=[1, 2, 3, 4, 5]
sqrList=map(square, numbers)
print(next(sqrList))
print(next(sqrList))
print(next(sqrList))
print(next(sqrList))
print(next(sqrList))

# In the above example, the map() function applies to each element in the numbers[] list. 
# This will return a map object which is iterable and so, we can use the next() function to traverse the list.

sqrList2 = map(lambda x: x*x, [1, 2, 3, 4])
print(list(sqrList2))

my_list = [2,3,4,5,6,7,8,9]
updated_list = map(square, my_list)
print(updated_list)
print(list(updated_list))

my_list = [2.6743,3.63526,4.2325,5.9687967,6.3265,7.6988,8.232,9.6907]
updated_list = map(round, my_list)
print(updated_list)
print(list(updated_list))


def myMapFunc(s):
    return s.upper()


my_str = "welcome to guru99 tutorials!"
updated_list = map(myMapFunc, my_str)
print(updated_list)
for i in updated_list:
    print(i, end="")


my_tuple = ('php','java','python','c++','c')

updated_list = map(myMapFunc, my_tuple)
print(updated_list)
print(list(updated_list))


def myMapFunc10(n):
    return n*10
my_dict = {2,3,4,5,6,7,8,9}
finalitems = map(myMapFunc10, my_dict)
print(finalitems)
print(list(finalitems))

# Add two lists using map and lambda 

numbers1 = [1, 2, 3] 
numbers2 = [4, 5, 6] 

result = map(lambda x, y: x + y, numbers1, numbers2) 
print(list(result)) 

# List of strings 
l = ['sat', 'bat', 'cat', 'mat'] 

# map() can listify the list of strings individually 
test = list(map(list, l)) 
print(test) 

aquarium_creatures = [
    {"name": "sammy", "species": "shark", "tank number": 11, "type": "fish"},
    {"name": "ashley", "species": "crab", "tank number": 25, "type": "shellfish"},
    {"name": "jo", "species": "guppy", "tank number": 18, "type": "fish"},
    {"name": "jackie", "species": "lobster", "tank number": 21, "type": "shellfish"},
    {"name": "charlie", "species": "clownfish", "tank number": 12, "type": "fish"},
    {"name": "olly", "species": "green turtle", "tank number": 34, "type": "turtle"}
]
def assign_to_tank(aquarium_creatures, new_tank_number):
    def apply(x):
        x["tank number"] = new_tank_number
        return x
    return map(apply, aquarium_creatures)

assigned_tanks = assign_to_tank(aquarium_creatures, 42)
print(list(assigned_tanks))