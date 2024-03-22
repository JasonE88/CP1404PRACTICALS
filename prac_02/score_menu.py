MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100
EXCELLENT_SCORE = 90
PASSABLE_SCORE = 50


def main():
    score = get_valid_score()
    menu = """
    (G)et a valid score
    (P)rint result
    (S)how stars
    (Q)uit
    """
    choice = input(menu + "\nEnter your choice: ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print_result(score)
        elif choice == "S":
            show_stars(score)
        else:
            print("Invalid choice. Please try again.")

        choice = input("\n" + menu + "\nEnter your choice: ").upper()

    print("Farewell!")


def determine_result(score):
    """Determine the result based on the score."""
    if score < MINIMUM_SCORE or score > MAXIMUM_SCORE:
        return "Invalid Score"
    elif score >= EXCELLENT_SCORE:
        return "Excellent"
    elif score >= PASSABLE_SCORE:
        return "Passable"
    else:
        return "Bad"


def get_valid_score():
    """Get a valid score from the user."""
    while True:
        try:
            score = float(input("Enter a score (0-100): "))
            if MINIMUM_SCORE <= score <= MAXIMUM_SCORE:
                return score
            else:
                print("Score must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def print_result(score):
    """Print the result based on the score."""
    print("Result:", determine_result(score))


def show_stars(score):
    """Show stars based on the score."""
    print("*" * int(score))


main()
