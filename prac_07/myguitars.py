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
