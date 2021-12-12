from functools import lru_cache


@lru_cache(maxsize=1000)
def fibonacci_lru_cache(nth):
    """Calculate the nth number in the fibonacci sequence
    Use lru_cache from functools to provide performance caching
    """

    # Check that the input is a positive integer
    if type(nth) != int:
        raise TypeError('n must be a positive integer')
    if nth < 1:
        raise ValueError('n must be a positive integer')

    # Compute the Nth term
    if nth == 1:
        return 1
    elif nth == 2:
        return 1
    elif nth > 2:
        return fibonacci_lru_cache(nth - 1) + fibonacci_lru_cache(nth - 2)


fibonacci_dict = {}


def fibonacci_cache(num):
    """Calculate the nth number in the fibonacci sequence
    Use custom dictionary to show caching
    """
    # if we have the cached value, then return it
    if num in fibonacci_dict:
        return fibonacci_dict[num]
    val = 0
    # Compute the Nth term
    if num == 1:
        val = 1
    elif num == 2:
        val = 1
    elif num > 2:
        val = fibonacci_cache(num - 1) + fibonacci_cache(num - 2)

    # Cache the value and return it
    fibonacci_dict[num] = val
    return val


def fibonacci_no_cache(n):
    """Calculate the nth number in the fibonacci sequence.
    No caching, performance will slow, Try 40
    """
    # Compute the Nth term
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci_no_cache(n - 1) + fibonacci_no_cache(n - 2)


print(80 * '-')
print("fibonacci without caching")

# for n in range(1, 41):
#     print(n, ':', fibonacci_no_cache(n))

print(80 * '-')
print("fibonacci with caching")

for i in range(1, 51):
    print(i, ':', fibonacci_cache(i))

print(80 * '-')
print("fibonacci with lru caching")

for i in range(1, 51):
    print(i, ':', fibonacci_lru_cache(i))

print("Ratios")

for i in range(1, 51):
    print(i, ':', fibonacci_lru_cache(i + 1) / fibonacci_lru_cache(i))


print(80 * '-')
print("fibonacci(100)", fibonacci_lru_cache(100))
print("fibonacci(500)", fibonacci_lru_cache(500))
