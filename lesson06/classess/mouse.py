class Mouse:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def print(self):
        print("**********")
        print("Mouse :", self.name, self.weight)


    def __str__(self):
        return f"{self.name}, {self.weight}"

