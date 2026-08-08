from entities.parking_spot import ParkingSpot
from entities.vehicle import Car,Bike
from enums.parking_enums import SpotType

car_spot= ParkingSpot("car_spot",SpotType.CAR)
car = Car("OD02AB1234","red")
bike = Bike("OD02AB5678","blue")

print("Initial availability:", car_spot.is_available())  # True

car_spot.park_vehicle(car)
print("After parking car:", car_spot.is_available())  # False

print("Can bike park here?:", car_spot.can_park(bike))  # False

try:
    car_spot.park_vehicle(bike)
except ValueError as e:
    print("Expected Error Caught:", e)

removed_vehicle = car_spot.remove_vehicle()
print("Removed vehicle:", removed_vehicle.license_number)
print("Final availability:", car_spot.is_available())  # True