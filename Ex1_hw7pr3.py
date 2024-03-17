ef power(b, p):
    '''
    Argument:
    '''
    if p == 0:  # Check if the power is 0
        x = 1  # If the power is 0, set the result to 1
        return x  # Return the result
    x = b  # If the power is not 0, initialize x to the base value 'b'
    result = x  # Initialize the 'result' variable to 'x'
    for y in range(p - 1):  # Iterate 'p - 1' times
        result = x * result  # Multiply 'result' by 'x' and update 'result'
    return result  # Return the final result after exponentiation

power(2, 0)  # Call the 'power()' function with base 2 and power 0
#Tests
print("power(2, 5): should be 32 ==", power(2, 5))
print("power(5, 2): should be 25 ==", power(5, 2))
print("power(42, 0): should be 1 ==", power(42, 0))
print("power(0, 42): should be 0 ==", power(0, 42))
print("power(0, 0): should be 1 ==", power(0, 0))
def summedOdds(L):
    """Loop-based function to return the sum of odd numbers in a list."""
    result = 0  # Initialize a variable to store the sum of odd numbers
    for e in L:  # Iterate through each element 'e' in the input list 'L'
        if e % 2 != 0:  # Check if the element is odd by checking if its remainder when divided by 2 is not zero
            result += e  # If the element is odd, add it to the result variable
    return result  # Return the sum of odd numbers

# Test cases
assert summedOdds([4, 5, 6]) == 5  # Test if the function returns the correct sum of odd numbers in the list [4, 5, 6]
assert summedOdds(range(3, 10)) == 24  # Test if the function returns the correct sum of odd numbers in the range from 3 to 9

# The above assertions will pass silently if the function behaves as expected
