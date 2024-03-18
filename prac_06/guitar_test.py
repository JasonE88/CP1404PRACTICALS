from guitar import Guitar

def run_tests():
    """Run tests for Guitar class."""
    # Test Guitar 1
    guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    print(f"{guitar1.name} get_age() - Expected 100. Got {guitar1.get_age()}")
    print(f"{guitar1.name} is_vintage() - Expected True. Got {guitar1.is_vintage()}")
