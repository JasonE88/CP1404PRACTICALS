# Estimate: 60 minutes
# Actual:  minutes

import datetime

class Project:
    """Represents a project with name, start date, priority, estimate, and completion attributes."""

    def __init__(self, name, start_date, priority, estimate, completion):
        """Initialize a Project instance."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.estimate = estimate
        self.completion = completion

    # Implement methods to load and save projects from/to a data file

    def load_projects(filename):
        """Load projects from a data file."""
        # Implement loading projects from the data file
        pass

    def save_projects(filename, projects):
        """Save projects to a data file."""
        # Implement saving projects to the data file
        pass