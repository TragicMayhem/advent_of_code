# Sets
example = set()   # rather than {}
odds = {1, 3, 5, 7, 9}
evens = {2, 4, 6, 8, 10}
primes = {2, 3, 5, 7}
composites = {4, 6, 8, 9, 10}  # use literal rather than set([4, 6, 8, 9, 10])

print(dir(primes))
print(help(example.add))

print("\nSets Basics")
example.add(42)
example.add("hello")
example.add(False)
example.add(3.14)
print(example)
print("example length", len(example))

print("example.add(42) again", example.add(42))
print("example length", len(example))
# example.remove will raise errors for missing
print("example.discard(42)", example.discard(42))
print("example.discard(50)", example.discard(50))

print("\n")

a = set('abracadabra')
b = set('alacazam')
print("a", a)
print("b", b)
print("AND a & b", a & b)
print("a | b OR inc BOTH", a | b)
print("a ^ b OR excl BOTH", a ^ b)

print(80 * '-')
print("\nSets")
print("odds", odds)
print("evens", evens)
print("primes", primes)
print("composites", composites)

print("\nUnion")
print("odds.union(evens)", odds.union(evens))
print("evens.union(odds)", evens.union(odds))

print("\nIntersection")
print("odds.intersection(primes)", odds.intersection(primes))
print("primes.intersection(evens)", primes.intersection(evens))
print("evens.intersection(odds)", evens.intersection(odds))

print("primes.union(composites)", primes.union(composites))

print("\nMisc")
print("6 in odds", 6 in odds)
print("2 in primes", 2 in primes)
