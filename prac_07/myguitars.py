from guitar import Guitar


def main():
    """Main function."""
    filename = "guitars.csv"

    # Load guitars from file
    guitars = Guitar.load_guitars(filename)

    # Display guitars
    display_guitars(guitars)

    # Add new guitars
    add_new_guitars(guitars)

    # Write guitars to file
    Guitar.write_guitars(filename, guitars)
    print("Guitars written to file.")


def display_guitars(guitars):
    """Display guitars."""
    print("Guitars:")
    for i, guitar in enumerate(guitars, 1):
        print(f"{i}. {guitar}")


def add_new_guitars(guitars):
    """Add new guitars."""
    while True:
        name = input("Enter guitar name (blank to quit): ")
        if not name:
            break
        year = int(input("Enter year made: "))
        cost = float(input("Enter cost: "))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)


if __name__ == "__main__":
    main()
