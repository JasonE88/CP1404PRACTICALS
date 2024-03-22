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
