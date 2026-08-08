from typing import Optional
from enums.parking_enums import SpotType
from entities.vehicle import Vehicle

class ParkingSpot:
    def __init__(self, spot_id:str, spot_type:SpotType):
        self.spot_id = spot_id
        self.spot_type = spot_type
        self.vehicle : Optional[Vehicle]=None

    def is_available(self) -> bool:
        return self.vehicle is None

    def can_park(self, vehicle:Vehicle) -> bool:
        return self.is_available() and vehicle.vehicle_type.value == self.spot_type.value

    def park_vehicle(self, vehicle:Vehicle):
        if not self.can_park(vehicle):
            raise ValueError(f"Cannot park vehicle of type {vehicle.vehicle_type} in spot of type {self.spot_type}")
        self.vehicle = vehicle

    def remove_vehicle(self) -> Vehicle:
        if self.vehicle is None:
            raise ValueError(
                f"Spot {self.spot_id} is already empty"
            )

        vehicle = self.vehicle
        self.vehicle = None

        return vehicle