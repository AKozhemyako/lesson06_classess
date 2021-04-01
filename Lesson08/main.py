from Lesson08.vehicle import *

if __name__ == '__main__':
    vehicle_list = [Plane(Point(1, 2), 10000, 200, 1990, 20, 15),
                    Plane(Point(2, 3), 10000, 200, 1990, 20, 25),
                    Ship(Point(4, 3), 20000, 200, 2000, "Odessa", 150),
                    Car(Point(4, 5), 5000, 200, 2001)
                    ]
    print(vehicle_list)
    for vehicle in vehicle_list:
        vehicle.show_image()