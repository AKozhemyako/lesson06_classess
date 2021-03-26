class Mouse:
    def __init__(self, name="Jerry", year=1, weight=0.5):
        self.name = name
        self.year = year
        self.weight = weight

    def print(self):
        print("**********")
        print("Mouse :", self.name, self.year, self.weight)


class MouseDoctorController:
    def __init__(self, mouse):
        self.OLD_MOUSE = 4
        self.YUNG_MOUSE = 1
        self.MIDDLE_MOUSE = 2
        self.mouse = mouse

    def diagnostic_age(self):
        if self.mouse.year < self.YUNG_MOUSE:
            print("Jung Mouse")
        elif self.mouse.year < self.MIDDLE_MOUSE:
            print("Junior Mouse")
        elif self.mouse.year < self.OLD_MOUSE:
            print("Old Mouse")


class MouseEatController:
    def __init__(self, mouse):
        self.mouse = mouse

    def max_food_limit(self):
        return self.mouse.weight / 2

    def min_food_limit(self):
        return 0

    def eat(self, food):
        if (self.min_food_limit() < food < self.max_food_limit()):
            self.mouse.weight += food
            return True
        else:
            print("Error food not in range (", self.mouse.min_food_limit(), "-", self.mouse.max_food_limit(), ")")
            return False

    def eat_from_console(self):
        while True:
            food = Helper().input_int_from_console()
            if self.eat(food):
                break