tuple_list = [("a", "b"),("c", "d")]
first_tuple_elements = []

print(tuple_list)

for a_tuple in tuple_list:
    first_tuple_elements.append(a_tuple[0])
print(first_tuple_elements)

first_tuple_elements = [a_tuple[0] for a_tuple in tuple_list]
print(first_tuple_elements)