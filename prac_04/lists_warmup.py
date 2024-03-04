numbers = [3, 1, 4, 1, 5, 9, 2]

print(numbers[0])           # Output: 3
print(numbers[-1])          # Output: 2
print(numbers[3])           # Output: 1
print(numbers[:-1])         # Output: [3, 1, 4, 1, 5, 9]
print(numbers[3:4])         # Output: [1]
print(5 in numbers)         # Output: True
print(7 in numbers)         # Output: False
print("3" in numbers)       # Output: False
print(numbers + [6, 5, 3])  # Output: [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

numbers[0] = "ten"         # Change the first element to "ten"
numbers[-1] = 1            # Change the last element to 1
print(numbers[2:])         # Print all elements except the first two
print(9 in numbers)        # Print whether 9 is an element of numbers



