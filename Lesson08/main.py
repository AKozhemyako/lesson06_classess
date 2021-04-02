from Lesson08.vehicle import *
from Lesson08.vehiclecontrol import VehicleControl

if __name__ == '__main__':
    vehicle_list = []
    print(vehicle_list)
    for vehicle in vehicle_list:
        vehicle.show_image()

    VehicleControl().print_max_price_vehicle(vehicle_list)