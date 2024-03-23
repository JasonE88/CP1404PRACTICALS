import datetime

class Project:
    """Represents a project with attributes such as name, start date, priority, estimate, and completion."""

    def __init__(self, name, start_date, priority, estimate, completion):
        """Initialize a Project object with given attributes."""
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = priority
        self.estimate = estimate
        self.completion = completion

    def __str__(self):
        """Return a string representation of the project."""
        return f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority {self.priority}, estimate: ${self.estimate:.2f}, completion: {self.completion}%"

    def update_completion(self, new_completion):
        """Update the completion percentage of the project."""
        self.completion = new_completion

    def update_priority(self, new_priority):
        """Update the priority of the project."""
        self.priority = new_priority

    def get_priority(self):
        """Get the priority of the project."""
        return self.priority
