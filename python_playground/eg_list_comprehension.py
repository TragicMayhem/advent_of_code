# [ expr for val in collection ]
# [ expr for val in collection if <test> ]

squares = []
for i in range(1, 101):
    squares.append(i**2)

print(squares)

squares2 = [i**2 for i in range(1, 101)]
print(squares2)

# -----

remainders5 = [x**2 % 5 for x in range(1, 101)]
print(remainders5)

remainders11 = [x**2 % 11 for x in range(1, 101)]
print(remainders11)

# -----
movies = ["Citizen Kane",
          "Groundhog Day",
          "Close encounters of the third kind",
          "Raiders of the lost ark"]

movies_with_years = [("Citizen Kane", 1941),
          ("Groundhog Day", 1993),
          ("Close encounters of the third kind", 1977),
          ("Raiders of the lost ark", 1981)]

cmovies = [title for title in movies if title.startswith("C")]
print(cmovies)

pre90movies = [title for (title, year) in movies_with_years if year < 1990]
print(pre90movies)

A = [1, 3, 5, 7]
B = [2, 4, 6, 8]

cartesian_product = [(a, b) for a in A for b in B]
print(cartesian_product)