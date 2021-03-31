from lesson06.classess.helper import Helper


class Cat:
    def __init__(self, name="Tom", year=6, weight=5):
        self.__name = name
        self.__year = year
        self.__weight = weight

    def get_name(self):
        return self.__name

    def get_year(self):
        return self.__year

    def set_weight(self, value):
        try:
            int_value = float(value)
            if int_value > 0:
                self.__weight = value
        except:
            print("Error")

    def get_weight(self):
        return self.__weight

    def __str__(self):
        return f"Cat: {self.get_name()}, {self.get_year()}, {self.get_weight()}"


class CatDoctorController:
    KITTEN_AGE = 1
    MIDDLE_CAT = 5
    OLD_CAT = 15

    def __init__(self, cat):
        self.cat = cat

    def diagnostic_age(self):
        if self.cat.get_year() < self.KITTEN_AGE:
            print("Kitten")
        elif self.cat.get_year() < self.MIDDLE_CAT:
            print("Junior Cat")
        elif self.cat.get_year() < self.OLD_CAT:
            print("Old Cat")


class CatEatController:
    def __init__(self, cat):
        self.cat = cat

    def max_food_limit(self):
        return self.cat.get_weight() / 2

    def min_food_limit(self):
        return 0

    def eat_mouse(self, mouse):
        self.eat(mouse.get_weight())
        mouse.set_weight(0)
        mouse.set_killer(self.cat)

    def eat(self, food):
        if (self.min_food_limit() < food < self.max_food_limit()):
            self.cat.set_weight(self.cat.get_weight() + food)
            return True
        else:
            print("Error food not in range (", self.cat.min_food_limit, "-", self.cat.max_food_limit(), ")")
            return False

    def eat_from_console(self):
        while True:
            food = input_float_from_console()
            if self.eat(food):
                break
