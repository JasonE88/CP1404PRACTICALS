from prac_09.car import Car
import random


class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car if random number is less than reliability."""
        random_number = random.randint(0, 100)
        if random_number < self.reliability:
            distance_driven = super().drive(distance)
        else:
            distance_driven = 0
        return distance_driven
