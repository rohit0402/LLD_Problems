from entities.vehicle import Car, Bike,Truck,Vehicle
from enums.parking_enums import VehicleType

#@staticmethod is used to define a static method, which means it can be called without creating an instance of the class.
# This is useful for utility functions that do not require state or instance variables.
class VehicleFactory:
    @staticmethod
    def create_vehicle(vehicle_type:VehicleType, license_number:str, color:str) -> Vehicle:
        if vehicle_type == VehicleType.BIKE:
            return Bike(license_number,color)
        elif vehicle_type == VehicleType.CAR:
            return Car(license_number,color)
        elif vehicle_type == VehicleType.TRUCK:
            return Truck(license_number,color)
        else:
            raise ValueError(f"Unsupported vehicle type: {vehicle_type}")