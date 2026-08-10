from entities.elevator import Elevator
from entities.elevator_request import ElevatorRequest

from enums.elevator_enums import Direction
from strategies.nearest_elevator_strategy import NearestElevatorStrategy
from services.elevator_system import ElevatorSystem

#create strategy
selector=NearestElevatorStrategy()

#create system
system=ElevatorSystem(selector)

#create elevators
elevator1=Elevator(1,0)
elevator2=Elevator(2,5)
elevator3=Elevator(3,10)

system.add_elevator(elevator1)
system.add_elevator(elevator2)
system.add_elevator(elevator3)

#user at 7 floor and want to go up
request=ElevatorRequest(source_floor=3,direction=Direction.DOWN)

#request elevator
elevator=system.request_elevator(request)

print(f"Elevator {elevator.elevator_id} "
    f"arrived at floor "
    f"{elevator.current_floor}")