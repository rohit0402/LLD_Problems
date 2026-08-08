from typing import List, Optional
from entities.parking_floor import ParkingFloor
from entities.parking_spot import ParkingSpot
from entities.vehicle import Vehicle

class ParkingLot:
    def __init__(self,lot_id:str):
        self.lot_id = lot_id
        self.floors : List[ParkingFloor] = []
        self.parked_vehicles=set()

    def is_vehicle_parked(self, license_number:str) -> bool:
        return license_number in self.parked_vehicles

    def add_floor(self, floor:ParkingFloor) ->None:
        self.floors.append(floor)

    def find_available_spot(self, vehicle:Vehicle) -> Optional[ParkingSpot]:
        for floor in self.floors:
            spot = floor.find_available_spot(vehicle)
            if spot is not None:
                return spot
        return None

    def remove_vehicle(self, license_number: str) -> None:
        self.parked_vehicles.remove(license_number)