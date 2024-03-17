def power(b, p):
    '''
    Argument:
    '''
    if p==0:
        x=1
        return x
    x=b
    result=x
    for y in range(p-1):
        result=x*result
    return result
power(2,0)
#Tests
print("power(2, 5): should be 32 ==", power(2, 5))
print("power(5, 2): should be 25 ==", power(5, 2))
print("power(42, 0): should be 1 ==", power(42, 0))
print("power(0, 42): should be 0 ==", power(0, 42))
print("power(0, 0): should be 1 ==", power(0, 0))
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
