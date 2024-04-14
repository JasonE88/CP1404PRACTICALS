from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    """Test the SilverServiceTaxi class."""

    my_taxi = SilverServiceTaxi("Silver Bird", 100, 2)

    my_taxi.drive(18)

    print(my_taxi)

    print(my_taxi.get_fare())


main()
