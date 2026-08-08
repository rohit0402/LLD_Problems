from typing import List,Optional
from entities.parking_spot import ParkingSpot
from entities.vehicle import Vehicle

class ParkingFloor:
    def __init__(self,floor_id:int):
        self.floor_id = floor_id
        self.spots : List[ParkingSpot] = []

    def add_spot(self, spot:ParkingSpot):
        self.spots.append(spot)

#here optional is used to return None if the vehicle cannot be parked in any of the spots
# if we return a spot, we will return the spot
    def find_available_spot(self, vehicle:Vehicle) -> Optional[ParkingSpot]:
        for spot in self.spots:
            if spot.can_park(vehicle):
                return spot
        return None