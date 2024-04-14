from prac_09.taxi import Taxi


def main():
    """Test the Taxi class."""
    my_taxi = Taxi("Prius 1", 100)

    my_taxi.drive(40)

    print(f"Taxi details:\n{my_taxi}\nCurrent fare: ${my_taxi.get_fare():.2f}\n")

    my_taxi.start_fare()
    my_taxi.drive(100)

    print(f"Taxi details:\n{my_taxi}\nCurrent fare: ${my_taxi.get_fare():.2f}\n")


main()
