from guitar import Guitar


def main():
    """Client program to input and display guitar details."""
    print("My guitars!")
    guitars = []
    while True:
        name = input("Name: ")
        if not name:
            break
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added.")

    print("\nThese are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_label = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar}, worth ${guitar.cost:.2f}{vintage_label}")


main()
