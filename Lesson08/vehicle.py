class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Vehicle:
    def __int__(self, point, price, speed, year):
        self.point = point
        self.price = price
        self.speed = speed
        self.year = year


class Plane(Vehicle):
    def __init__(self, point, price, speed, year, height, count_pass):
        super().__init__(point, price, speed, year)
        self.height = height
        self.count_pass = count_pass


class Ship(Vehicle):
    def __int__(self, point, price, speed, year, port, count_pass):
        super().__int__(point, price, speed, year)
        self.port = port
        self.count_pass = count_pass


class Car(Vehicle):
    def __int__(self, point, price, speed, year):
        super().__int__(point, price, speed, year)


