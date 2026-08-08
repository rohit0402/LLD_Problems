from datetime import datetime
from typing import Optional

from entities.parking_spot import ParkingSpot
from entities.vehicle import Vehicle

class Ticket:
    def __init__(self,ticket_id:str, vehicle:Vehicle, spot:ParkingSpot):
        self.ticket_id = ticket_id
        self.vehicle = vehicle
        self.spot = spot
        self.entry_time = datetime.now()
        self.exit_time : Optional[datetime] = None

