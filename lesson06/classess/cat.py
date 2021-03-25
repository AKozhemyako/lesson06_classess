class Cat:
    def __init__(self, name="Tom", year=6, weight=7):
        self.name = name
        self.year = year
        self.weight = weight

    def print(self):
        print("**********")
        print("Cat: ", "Name:", self.name, "Age:", self.year, "Weight:", self.weight)
