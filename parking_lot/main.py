from entities.parking_lot import ParkingLot
from entities.parking_spot import ParkingSpot
from entities.parking_floor import ParkingFloor

from enums.parking_enums import SpotType, VehicleType
from factories.vehicle_factory import VehicleFactory

from strategies.payment_strategies import CardPaymentStrategy

from services.parking_service import ParkingService
from services.fee_calculator import FeeCalculator
from services.payment_service import PaymentService

# SETUP
print("=" * 60)
print("PARKING LOT TEST SUITE")
print("=" * 60)

# Create Parking Lot
parking_lot = ParkingLot("Lot1")
# Create Floor
floor1 = ParkingFloor(1)
# Add Spots
floor1.add_spot(    ParkingSpot("C-101", SpotType.CAR))

floor1.add_spot(    ParkingSpot("B-101", SpotType.BIKE))

floor1.add_spot(    ParkingSpot("T-101", SpotType.TRUCK))

# Add Floor to Parking Lot
parking_lot.add_floor(floor1)


# Create Services
fee_calculator = FeeCalculator()

payment_service = PaymentService(    CardPaymentStrategy())

parking_service = ParkingService(    parking_lot,fee_calculator,    payment_service)


# TEST 1 — NORMAL CAR PARKING

print("\n[TEST 1] Normal Car Parking")

car1 = VehicleFactory.create_vehicle(    VehicleType.CAR,    "OD02AB1234",    "Red")

ticket1 = parking_service.park_vehicle(    car1,    "TICKET-001")

print(    f"PASS: Vehicle {car1.license_number} "    f"parked at {ticket1.spot.spot_id}")

# TEST 2 — DUPLICATE VEHICLE

print("\n[TEST 2] Duplicate Vehicle")
try:
    parking_service.park_vehicle(    car1,        "TICKET-002"    )
    print("FAIL: Duplicate vehicle was allowed")
except ValueError as e:
    print(f"PASS: {e}")

# TEST 3 — NO AVAILABLE CAR SPOT
print("\n[TEST 3] No Available Car Spot")

car2 = VehicleFactory.create_vehicle(VehicleType.CAR,    "OD02XY5678",    "Blue")

try:
    parking_service.park_vehicle(    car2,        "TICKET-002")
    print("FAIL: Vehicle parked despite no available spot")
except ValueError as e:
    print(f"PASS: {e}")

# TEST 4 — CAR EXIT
print("\n[TEST 4] Car Exit")
fee1 = parking_service.unpark_vehicle(    ticket1)

print(    f"PASS: Car exited successfully. "    f"Fee paid: ₹{fee1}")

# TEST 5 — EXIT SAME TICKET AGAIN
print("\n[TEST 5] Exit Same Ticket Again")
try:
    parking_service.unpark_vehicle(    ticket1)
    print("FAIL: Closed ticket was accepted")
except ValueError as e:
    print(f"PASS: {e}")

# TEST 6 — SPOT REUSE
print("\n[TEST 6] Spot Reuse")
car3 = VehicleFactory.create_vehicle(    VehicleType.CAR,    "OD02ZZ9999",    "White")

ticket3 = parking_service.park_vehicle(    car3,    "TICKET-003")

if ticket3.spot.spot_id == "C-101":
    print(        f"PASS: Released spot C-101 reused by "        f"{car3.license_number}")
else:
    print(        f"FAIL: Expected C-101 but got "        f"{ticket3.spot.spot_id}")

# TEST 7 — BIKE + CORRECT FEE STRATEGY
print("\n[TEST 7] Bike Fee Strategy")

bike = VehicleFactory.create_vehicle(VehicleType.BIKE,    "OD01AA1111",    "Black")

bike_ticket = parking_service.park_vehicle(    bike,    "TICKET-004")

bike_fee = parking_service.unpark_vehicle(    bike_ticket)

if bike_fee == 20:
    print(        f"PASS: Bike fee strategy applied correctly. "        f"Fee: ₹{bike_fee}")
else:
    print(   f"FAIL: Expected ₹20 but got ₹{bike_fee}")

# TEST 8 — TRUCK + CORRECT FEE STRATEGY
print("\n[TEST 8] Truck Fee Strategy")

truck = VehicleFactory.create_vehicle(    VehicleType.TRUCK,    "OD03BB2222",    "White")

truck_ticket = parking_service.park_vehicle(    truck,    "TICKET-005")

truck_fee = parking_service.unpark_vehicle(    truck_ticket)

if truck_fee == 60:
    print(
        f"PASS: Truck fee strategy applied correctly. "
        f"Fee: ₹{truck_fee}"
    )
else:
    print(
        f"FAIL: Expected ₹60 but got ₹{truck_fee}"
    )

# FINAL STATE
print("\n" + "=" * 60)
print("ALL TESTS COMPLETED")
print("=" * 60)