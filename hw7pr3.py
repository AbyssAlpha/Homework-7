def summedOdds(L):
    """Loop-based function to return the sum of odd numbers in a list."""
    result = 0
    for e in L:
        if e % 2 != 0:
            result += e
    return result
#Tests
assert summedOdds([4, 5, 6]) == 5
assert summedOdds(range(3, 10)) == 24
