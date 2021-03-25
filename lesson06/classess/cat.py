class Cat:
    def __init__(self, name="Tom", year=6, weight=7):
        self.name = name
        self.year = year
        self.weight = weight

    def max_food_limit(self):
        return self.weight/3

    def min_food_limit(self):
        return self.weight / 7

    def eat(self, food):
        if (0<food<self.max_food_limit()):
            self.weight+=food
        else:
            print("Error food not in range (", self.min_food_limit(), "-" ,self.max_food_limit(), ")" )


    def print(self):
        print("**********")
        print("Cat: ", "Name:", self.name, "Age:", self.year, "Weight:", self.weight)
