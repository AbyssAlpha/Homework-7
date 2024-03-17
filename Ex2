def unique(L):
    """Checks if all elements in the list L are unique."""
    return len(L) == len(set(L))

def untilARepeat(high):
    """Counts the number of guesses needed until a repeat is encountered."""
    L = []  # Initialize the list to store guessed integers
    count = 0  # Initialize a counting variable for the number of guesses
    
    while unique(L):  # Keep looping as long as all elements in L are unique
        guess = random.choice(range(0, high + 1))  # Make a guess in the range(0, high)
        count += 1  # Increase the count of guesses by 1
        L.append(guess)  # Add the guess to the end of the list L
        
    return count  # Return the number of guesses needed until a repeat is encountered

# Test the function
print(untilARepeat(99))  # Example usage with high=99
