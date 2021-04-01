class Vehicle:
    def __int__(self, point, price, speed, year):
        self.point = point
        self.price = price
        self.speed = speed
        self.year = year

class Plane(Vehicle):
    def __init__(self, point, price, speed, year, height, count_pass):
        super(Plane, self).__init__()
        self.height = height
        self.count_pass = count_pass