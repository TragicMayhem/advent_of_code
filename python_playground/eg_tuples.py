import sys
import timeit

primes = [2, 3, 5, 7, 11, 13]
perfect_squares = (1, 4, 9, 16, 25, 36)

print("# squares =", len(perfect_squares))
for n in perfect_squares:
    print("Sq:", n)

print("\nDifferences List/Tuple")
print(dir(primes))
print(dir(perfect_squares))

print("\n")
list_eg = [1, 2, 3, "a", "b", "c", True, 3.14159]
tuple_eg = (1, 2, 3, "a", "b", "c", True, 3.14159)

print("List size=", sys.getsizeof(list_eg))
print("Tuple size=", sys.getsizeof(tuple_eg))

print("\n")
test_list = timeit.timeit(stmt="[1, 2, 3, 4, 5]",
                          number=1000)
test_tuple = timeit.timeit(stmt="(1, 2, 3, 4, 5)",
                           number=1000)

print("list time: ", test_list)
print("tuple time:", test_tuple)
print("list time:  {0:.8f}".format(test_list))
print("tuple time: {0:.8f}".format(test_tuple))
