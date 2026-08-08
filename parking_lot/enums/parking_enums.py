#Why did you use Enum instead of strings? I used enums for fixed domain values such as vehicle type, spot type, payment 
# method, and payment status. This provides type safety, avoids inconsistent string values, improves readability, and makes 
# the allowed states explicit.
# VehicleType and SpotType represent different domain concepts. A vehicle type describes the vehicle, while a spot type 
# describes the capacity or compatibility of a parking spot. Although their mapping is one-to-one under the current 
# requirements, keeping them separate allows the model to evolve independently.

from enum import Enum

class VehicleType(Enum):
    BIKE = "BIKE"
    CAR = "CAR"
    TRUCK = "TRUCK"


class SpotType(Enum):
    BIKE = "BIKE"
    CAR = "CAR"
    TRUCK = "TRUCK"


class PaymentMethod(Enum):
    CASH = "CASH"
    CARD = "CARD"


class PaymentStatus(Enum):
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"