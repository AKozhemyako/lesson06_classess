class VehicleControl:
    @staticmethod
    def print_max_price_vehicle(vehicle_list):
        max_price_vehicle = vehicle_list[0]
        for vehicle in vehicle_list:
            if vehicle.price > max_price_vehicle.price:
                max_price_vehicle = vehicle
        print(max_price_vehicle)
