from lesson06.classess.cat import Cat

if __name__ == '__main__':
    cat1 = Cat()
    cat1.print()

    cat2 = Cat("Tom2", 5, 5.5)
    cat2.print()

    cat3 = Cat(year=4, name="Tom3", weight=5.8)
    cat3.print()
