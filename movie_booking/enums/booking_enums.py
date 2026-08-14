from enum import Enum

class SeatStatus(Enum):
    AVAILABLE="AVAILABLE"
    BOOKED="BOOKED"

class BookingStatus(Enum):
    CONFIRMED="CONFIRMED"
    CANCELLED="CANCELLED"
    