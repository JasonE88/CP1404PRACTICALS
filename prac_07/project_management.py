from project import Project
import datetime


def main():
    """Main function."""
    print("Welcome to Pythonic Project Management")
    projects = Project.load_projects("projects.txt")
    print(f"Loaded {len(projects)} projects from projects.txt")
    menu(projects)


def menu(projects):
    """Display the menu and handle user input."""
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
            load_projects(projects)
        elif choice == 's':
            save_projects(projects)
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            filter_projects_by_date(projects)
        elif choice == 'a':
            add_new_project(projects)
        elif choice == 'u':
            update_project(projects)
        elif choice == 'q':
            quit_program(projects)
            break
        else:
            print("Invalid choice. Please try again.")


def load_projects(projects):
    """Load projects from a data file."""
    filename = input("Enter filename to load projects from: ")
    projects.extend(Project.load_projects(filename))
    print(f"Loaded {len(projects)} projects from {filename}")


def save_projects(projects):
    """Save projects to a data file."""
    filename = input("Enter filename to save projects to: ")
    Project.save_projects(filename, projects)
    print(f"Saved {len(projects)} projects to {filename}")


def display_projects(projects):
    """Display projects."""
    # Implement displaying projects
    pass


def filter_projects_by_date(projects):
    """Filter projects by date."""
    # Implement filtering projects by date
    pass


def add_new_project(projects):
    """Add a new project."""
    # Implement adding a new project
    pass


def update_project(projects):
    """Update a project."""
    # Implement updating a project
    pass


def quit_program(projects):
    """Quit the program."""
    choice = input("Would you like to save to projects.txt? ").strip().lower()
    if choice.startswith('y'):
        Project.save_projects("projects.txt", projects)
    print("Thank you for using custom-built project management software.")


if __name__ == "__main__":
    main()