#
#
#
#
#
#
#
#
#
#
#
import abc
from abc import ABC

from Lesson08.coordinate import *

class Passenger(metaclass=abc.ABCMeta):
    def __init__(self, count_pass):
        self.count_pass = count_pass

    @property
    def count_pass(self):
        return self.__count_pass

    @count_pass.setter
    def count_pass(self, value):
        if value > 0:
            self.__count_pass = value
        else:
            self.__count_pass = 0

class Vehicle(metaclass=abc.ABCMeta):
    def __int__(self, point: Point, price: float, speed: float, year: int):
        self.point = point
        self.price = price
        self.speed = speed
        self.year = year

    def __str__(self) -> str:
        return f"{self.point}, {self.price}, {self.speed}, {self.year}"

    @abc.abstractmethod
    def show_image(self):pass



class Plane(Vehicle):
    def __init__(self, point, price, speed, year, height, count_pass):
        super().__init__(point, price, speed, year)
        self.height = height
        self.count_pass = count_pass

    def __str__(self) -> str:
        return f"{super().__str__()},{self.height},{self.count_pass}"

    def __repr__(self) -> str:
        return f"\nPlane: {self.__str__()}"

    def show_image(self):
        print("Plane")


class Ship(Vehicle):
    def __int__(self, point, price, speed, year, port, count_pass):
        super().__int__(point, price, speed, year)
        self.port = port
        self.count_pass = count_pass

    def __str__(self) -> str:
        return f"{super().__str__()}. {self.port}, {self.count_pass}"

    def __repr__(self) -> str:
        return f"\nShip: {self.__str__()}"

    def show_image(self):
        print("Ship")

class Car(Vehicle):
    def __int__(self, point, price, speed, year):
        super().__int__(point, price, speed, year)

    def __repr__(self) -> str:
        return f"\nCar: {self.__str__()}"

    def show_image(self):
        pass


