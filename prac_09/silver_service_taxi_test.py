from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    """Test the SilverServiceTaxi."""
    my_taxi = SilverServiceTaxi("Hummer", 200, 4.92, 4)

    my_taxi.start_fare()
    my_taxi.drive(18)

    print(my_taxi)
    print("Fare: ${:.2f}".format(my_taxi.get_fare()))


main()
