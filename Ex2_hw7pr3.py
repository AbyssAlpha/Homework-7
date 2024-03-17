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
#The largest class size where no two persons have the same birthdate is 365 if there are 365 pupils in the class, each of whom was born on a different day of the year.
#The smallest class size that can exist and still have at least one pair of students with the same birthday is two students.
#The birthday paradox provides a non-linear explanation for the difference between the greatest and smallest class sizes and the average class size, which is usually approximately 23. According to the birthday paradox, there is a larger than 50% chance that at least two individuals in a group of twenty-three have the same birthday. The higher the group size, the faster this likelihood rises. It's not immediately obvious how many people are needed to have a 50% chance of having a birthday though.
