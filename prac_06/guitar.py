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