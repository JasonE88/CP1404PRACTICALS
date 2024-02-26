"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        print("Cannot divide by zero!")
    else:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")

#1. ValueError will occur when the user enters a non-integer value when prompted for the numerator or denominator
#2. ZeroDivisionError will occur if the user enters 0 as the denominator, leading to division by zero
#3. Yes, by adding a condition to check if the denominator is zero before performing the division operation. If the denominator is zero, we can handle it, such as printing an error message