import csv


class Guitar:
    """Represents a guitar with name, year, and cost attributes."""

    def __init__(self, name="", year=0, cost=0):
        """Initialize a Guitar instance.

        Parameters:
        - name: The name of the guitar.
        - year: The year the guitar was made.
        - cost: The cost of the guitar.
        """
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of the Guitar object."""
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"

    def get_age(self):
        """Return how old the guitar is in years."""
        return 2024 - self.year

    def is_vintage(self):
        """Return True if the guitar is 50 or more years old, False otherwise."""
        return self.get_age() >= 50

    def load_guitars(filename):
        """Load guitars from a CSV file and return a list of Guitar objects."""
        guitars = []
        with open(filename, "r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                name, year, cost = row
                year = int(year)
                cost = float(cost)
                guitar = Guitar(name, year, cost)
                guitars.append(guitar)
        return guitars

    def write_guitars(filename, guitars):
        """Write guitars to a CSV file."""
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            for guitar in guitars:
                writer.writerow([guitar.name, guitar.year, guitar.cost])

    load_guitars = staticmethod(load_guitars)
    write_guitars = staticmethod(write_guitars)
