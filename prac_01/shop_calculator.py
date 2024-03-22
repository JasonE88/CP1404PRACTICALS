NO_ITEMS = 0
PERCENTAGE = 0.1
MINIMUM_THRESHOLD_AMOUNT = 100
total_price = 0

number_of_items = int(input("Number of items: "))
while number_of_items < NO_ITEMS:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))
for item in range(number_of_items):
    item_price = float(input("Price of item: "))
    total_price += item_price
if total_price > MINIMUM_THRESHOLD_AMOUNT:
    total_price = total_price - (total_price * PERCENTAGE)
print(f"Total price for {number_of_items} items is ${total_price:.2f}")
