from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Represent a SilverServiceTaxi."""
    flagfall = 4.5

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        """Return a string representation of a SilverServiceTaxi."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        """Get the current fare."""
        return self.flagfall + super().get_fare()

"""
Inheriting Enhancements
class Taxi(Car):
    #Represent a Taxi object

    price_per_km = 1.23
    flagfall = 4.50

    def get_fare(self):
        #Return the price for the taxi trip, rounded to the nearest 10 cents.
        fare = super().get_fare() + self.flagfall
        return round(fare, 1)
"""