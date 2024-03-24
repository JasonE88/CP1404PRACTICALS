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


def load_projects(file_name):
    """Load projects from a file and return a list of Project objects."""
    projects = []
    with open(file_name, 'r') as file:
        next(file)  # Skip header line
        for line in file:
            name, start_date, priority, estimate, completion = line.strip().split('\t')
            projects.append(Project(name, start_date, int(priority), float(estimate), int(completion)))
    return projects


def save_projects(file_name, projects):
    """Save projects to a file."""
    with open(file_name, 'w') as file:
        file.write("Name\tStart Date\tPriority\tEstimate\tCompletion\n")
        for project in projects:
            file.write(
                f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t{project.estimate}\t{project.completion}\n")


def display_projects(projects):
    """Display incomplete and completed projects sorted by priority."""
    incomplete_projects = [project for project in projects if project.completion < 100]
    completed_projects = [project for project in projects if project.completion == 100]
    incomplete_projects.sort(key=lambda x: x.priority)
    completed_projects.sort(key=lambda x: x.priority)

    print("Incomplete projects:")
    for project in incomplete_projects:
        print(f"  {project}")

    print("Completed projects:")
    for project in completed_projects:
        print(f"  {project}")


def filter_projects_by_date(projects, date):
    """Filter projects starting after the given date and display them sorted by date."""
    filtered_projects = [project for project in projects if project.start_date > date]
    filtered_projects.sort(key=lambda x: x.start_date)

    print(f"Projects starting after {date.strftime('%d/%m/%Y')}:")
    for project in filtered_projects:
        print(f"  {project}")


def add_new_project(projects):
    """Add a new project to the list."""
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = int(input("Priority: "))
    estimate = float(input("Cost estimate: $"))
    completion = int(input("Percent complete: "))
    projects.append(Project(name, start_date, priority, estimate, completion))


def update_project(projects):
    """Update completion percentage and/or priority of a project."""
    print("Projects:")
    for i, project in enumerate(projects):
        print(f"{i}: {project}")

    choice = int(input("Project choice: "))
    project = projects[choice]

    new_completion = input("New completion percentage: ")
    if new_completion:
        project.update_completion(int(new_completion))

    new_priority = input("New priority: ")
    if new_priority:
        project.update_priority(int(new_priority))


def main():
    file_name = "projects.txt"
    projects = load_projects(file_name)

    print("Welcome to Pythonic Project Management")
    print(f"Loaded {len(projects)} projects from {file_name}")

    while True:
        print("\nMenu:")
        print("- (L)oad projects")
        print("- (S)ave projects")
        print("- (D)isplay projects")
        print("- (F)ilter projects by date")
        print("- (A)dd new project")
        print("- (U)pdate project")
        print("- (Q)uit")

        choice = input(">>> ").strip().lower()

        if choice == 'l':
            file_name = input("Enter filename to load projects from: ")
            projects = load_projects(file_name)
            print(f"Loaded {len(projects)} projects from {file_name}")
        elif choice == 's':
            file_name = input("Enter filename to save projects to: ")
            save_projects(file_name, projects)
            print(f"Projects saved to {file_name}")
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            date_string = input("Show projects that start after date (dd/mm/yyyy): ")
            date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
            filter_projects_by_date(projects, date)
        elif choice == 'a':
            add_new_project(projects)
        elif choice == 'u':
            update_project(projects)
        elif choice == 'q':
            save_choice = input("Would you like to save to projects.txt? ").strip().lower()
            if save_choice.startswith('y'):
                save_projects("projects.txt", projects)
                print("Projects saved to projects.txt")
            print("Thank you for using custom-built project management software.")
            break
        else:
            print("Invalid choice. Please select again.")


if __name__ == "__main__":
    main()