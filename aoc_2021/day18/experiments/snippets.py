import math

def check_explosion(items):
    
    big_numbers = [item for item in items if item > 10]
    return len(big_numbers)

def explode(number):
    '''
    If embedded in four pairs need to explode
        left number is added to the number to left
        right number is added to the number to the right
        then replace the pair with zero
    '''
    ln = math.floor(number / 2)
    rn = math.ceil(number / 2)
    return [ln,rn]


depth = lambda L: isinstance(L, list) and max(map(depth, L))+1
print('depth',depth([[1, 2], [[1, 2], 3], [9, [8, 7]], [[1, 9], [8, 5]], [[[[1, 2], [3, 4]], [[5, 6], [7, 8]]], 9], [[[9, [3, 8]], [[0, 9], 6]], [[[3, 7], [4, 9]], 3]], [[[[1, 3], [5, 3]], [[1, 3], [8, 7]]], [[[4, 9], [6, 9]], [[8, 2], [7, 3]]]]]))

print(explode(15))
print(explode(12))

test_list = [[1, 2], [[1, 2], 3], [9, [8, 7]], [[1, 9], [8, 5]], [[[[1, 2], [3, 4]], [[5, 6], [7, 8]]], 9]]
test_list2 = [[1, 2], [[1, 12], 3], [9, [8, 7]], [[1, 19], [8, 15]], [[[[1, 2], [13, 4]], [[5, 6], [7, 8]]], 9]]


def count_big_numbers(l):

    if isinstance(l, list):
        return 0 + sum(count_big_numbers(item) for item in l)
    else:
        if l > 10:
            return 1
        else:
            return 0

# count_big_numbers2 = lambda L: isinstance(L, list) and sum(map(count_big_numbers2, L))+1

print(count_big_numbers(test_list))
print(count_big_numbers(test_list2))
# print(count_big_numbers2(test_list2))


