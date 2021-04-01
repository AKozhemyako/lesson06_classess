from Lesson08.coordinate import Point


class Vehicle:
    def __int__(self, point:Point, price, speed, year):
        self.point = point
        self.price = price
        self.speed = speed
        self.year = year
    def __str__(self) -> str:
        return f"{self.point}, {self.price}, {self.speed}, {self.year}"


class Plane(Vehicle):
    def __init__(self, point, price, speed, year, height, count_pass):
        super().__init__(point, price, speed, year)
        self.height = height
        self.count_pass = count_pass

    def __str__(self) -> str:
        return f"{super().__str__()}. {self.height}, {self.count_pass}"


class Ship(Vehicle):
    def __int__(self, point, price, speed, year, port, count_pass):
        super().__int__(point, price, speed, year)
        self.port = port
        self.count_pass = count_pass


class Car(Vehicle):
    def __int__(self, point, price, speed, year):
        super().__int__(point, price, speed, year)


