from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    """Taxi simulator program."""
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    bill = 0.0

    print("Let's drive!")
    while True:
        display_menu(taxis, bill)
        choice = input(">>> ").lower()

        if choice == 'q':
            print(f"Total trip cost: ${bill:.2f}")
            print("Taxis are now:")
            for i, taxi in enumerate(taxis):
                print(f"{i} - {taxi}")
            break
        elif choice == 'c':
            current_taxi = choose_taxi(taxis)
        elif choice == 'd':
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                fare = drive_taxi(current_taxi)
                bill += fare
                print(f"Bill to date: ${bill:.2f}")
        else:
            print("Invalid option")


def display_menu(taxis, bill):
    """Display the menu options."""
    print(f"Bill to date: ${bill:.2f}")
    print("q)uit, c)hoose taxi, d)rive")