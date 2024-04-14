import random

# Line 1: You would see a random integer between 5 and 20 (inclusive).
# Smallest number: 5
# Largest number: 20

# Line 2: You would see a random odd integer between 3 and 9 (inclusive).
# Smallest number: 3
# Largest number: 9
# Line 2 could not produce a 4 since the step value is 2, and it would only produce odd integers.

# Line 3: You would see a random floating-point number between 2.5 and 5.5.
# Smallest number: 2.5
# Largest number: 5.5

# Code to produce a random number between 1 and 100 (inclusive)
random_number = random.randint(1, 100)
print(random_number)
