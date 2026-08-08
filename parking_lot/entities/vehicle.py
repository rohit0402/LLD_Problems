from enums.parking_enums import VehicleType
#ABC is used to define an abstract base class, which cannot be instantiated directly and serves as a blueprint for other 
# classes. 
# If Vehicle is abstract, shouldn't it have @abstractmethod? An abstract base class can be used simply to prevent/ discourage
#  direct instantiation and communicate design intent, but Python's ABC alone does not prevent instantiation. 
# modeling Vehicle as an abstraction, while not forcing artificial behavior just to satisfy an abstract-method requirement.
class Vehicle:
    def __init__(self, license_number:str, color:str, vehicle_type:VehicleType):
        self.license_number = license_number
        self.color = color
        self.vehicle_type = vehicle_type

#super() is used to call the parent class constructor and initialize the object with the provided parameters
class Bike(Vehicle):
    def __init__(self,license_number:str, color:str):
        super().__init__(license_number, color, VehicleType.BIKE)

class Car(Vehicle):
    def __init__(self,license_number:str, color:str):
        super().__init__(license_number,color,VehicleType.CAR)

class Truck(Vehicle):
    def __init__(self,license_number:str, color:str):
        super().__init__(license_number,color,VehicleType.TRUCK)

# Why inheritance instead of composition? Here the relationship is naturally an IS-A relationship: a Bike, Car, and 
# Truck are all Vehicles and share a common contract and attributes. Therefore inheritance is reasonable. 
# I would prefer composition when the relationship represents HAS-A or when behavior needs to be assembled dynamically.