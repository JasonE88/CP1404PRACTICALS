for j in range(0, 101, 10):
    print(j, end=' ')
print()
for k in range(20, 0, -1):
    print(k, end=' ')
print()
stars = int(input("Number of stars: "))
for star in range(0, stars):
    print("*", end="")
print()
for star in range(1, stars + 1):
    print("*" * star)