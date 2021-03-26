from lesson06.classess.cat import *
from lesson06.classess.helper import Helper

if __name__ == '__main__':
    cat1 = Cat()
    cat1.print()
    cat_eating = CatEatController(cat1)
    cat_eating.eat_from_console()
    cat1.print()

    cat_diag = CatDoctorController(cat1)
    cat_diag.diagnostic_age()

    cat2 = Cat("Tom2", 5, 5.5)
    cat2.print()
    CatDoctorController(cat1).diagnostic_age()

    cat3 = Cat(year=4, name="Tom3", weight=5.8)
    cat3.print()
    CatDoctorController(cat1).diagnostic_age()