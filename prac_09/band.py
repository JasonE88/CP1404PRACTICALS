class Band:
    """For storing details of a band."""

    def __init__(self, name=""):
        """Initialize a Band with a name and an empty list of musicians."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of a Band."""
        musician_info = ", ".join(str(musician) for musician in self.musicians)
        return f"{self.name} ({musician_info})"

    def add(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

    def play(self):
        """Simulate the band playing, returning a list of strings indicating who is playing what."""
        play_results = []
        for musician in self.musicians:
            play_results.append(musician.play())
        return play_results
