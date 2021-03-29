from lesson06.classess.cat import *
from lesson06.classess.mouse import Mouse

if __name__ == '__main__':
    cat1 = Cat()
    cat1.set_weight()
    print(cat1)

    cat_eating = CatEatController(cat1)
    cat_eating.eat_from_console()
    print(cat1)

    cat_diag = CatDoctorController(cat1)
    cat_diag.diagnostic_age()

    cat2 = Cat("Tom2", 5, 5.5)
    print(cat2)
    CatDoctorController(cat2).diagnostic_age()

    cat3 = Cat(year=4, name="Tom3", weight=5.8)
    print(cat3)
    CatDoctorController(cat3).diagnostic_age()

    mouse1 = Mouse("Jerry", 0.3)
    mouse1.print()
    print(mouse1.__str__)
