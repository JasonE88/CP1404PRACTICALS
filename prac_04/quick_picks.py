import random

MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_LINE = 6
QUICK_PICKS_HEADER = "How many quick picks? "

def main():
    """Generate and display quick picks for the lottery."""
    try:
        num_quick_picks = int(input(QUICK_PICKS_HEADER))
        quick_picks = [generate_quick_pick() for _ in range(num_quick_picks)]
        display_quick_picks(quick_picks)
    except ValueError:
        print("Please enter a valid number.")


def generate_quick_pick():
    """Generate a quick pick consisting of random numbers."""
    return sorted(random.sample(range(MIN_NUMBER, MAX_NUMBER + 1), NUMBERS_PER_LINE))


def display_quick_picks(quick_picks):
    """Display the generated quick picks."""
    for quick_pick in quick_picks:
        print(" ".join(f"{number:2}" for number in quick_pick))


main()