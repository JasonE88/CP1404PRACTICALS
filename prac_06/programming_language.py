# Estimate: 1 hour
# Actual: 1 hour 25 minutes

class ProgrammingLanguage:
    """Represents a programming language with various attributes."""

    def __init__(self, name, typing, reflection, year):
        """Initialize a ProgrammingLanguage object.

        Parameters:
        - name: The name of the programming language
        - typing: The typing style of the programming language
        - reflection: Indicates if the programming language supports reflection
        - year: The year the programming language was first introduced
        """
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Check if the programming language is dynamically typed"""
        return self.typing == "Dynamic"

    def __str__(self):
        """Return a string representation of the ProgrammingLanguage object."""
        reflection_str = "Reflection=True" if self.reflection else "Reflection=False"
        return f"{self.name}, {self.typing} Typing, {reflection_str}, First appeared in {self.year}"