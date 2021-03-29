class Helper:
    def input_int_from_console(self):
        while True:
            try:
                value = int(input("Enter int data value"))
                return value
            except:
                print("Error not int data")

    def input_float_from_console(self):
        while True:
            try:
                value = float(input("Enter float data value"))
                return value
            except:
                print("Error not float data")
