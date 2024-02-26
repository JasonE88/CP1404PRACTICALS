# Question 1
out_file = open("name.txt", "w")
name = input("Enter your name: ")
print(name, file=out_file)
out_file.close()

# Question 2
with open("name.txt", "r") as file:
    name = file.read().strip()
print(f"Your name is {name}")

# Question 3
with open("numbers.txt", "r") as file:
    number1 = int(file.readline().strip())
    number2 = int(file.readline().strip())
sum_of_numbers = number1 + number2
print("Sum of the first two numbers is:", sum_of_numbers)

# Question 4
total = 0

with open("numbers.txt", "r") as file:
    for line in file:
        total += int(line.strip())
print("Total of all numbers in numbers.txt is:", total)