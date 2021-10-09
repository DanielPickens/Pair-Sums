import math

def numberOfWays(arr, k):
    if not arr:
        return 0
    maps = {}
    counter = 0
    for num in arr:
        diff = k - num
        if num in maps:
            counter += maps[num]
            maps[num] += 1
        else:
            maps[diff] = 1
    return counter
