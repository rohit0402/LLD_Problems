from enums.elevator_enums import ElevatorState,Direction

class Elevator:
    def __init__(self,elevator_id:int,current_floor:int =0):
        self.elevator_id=elevator_id
        self.current_floor=current_floor

        self.state=ElevatorState.IDLE
        self.direction=Direction.IDLE

        self.destination=[]

    def add_destination(self,floor:int)->None:
        if floor not in self.destination:
            self.destination.append(floor)

    def move_to(self,floor:int)->None:
        if floor == self.current_floor:
            return 

        self.state=ElevatorState.MOVING

        if floor > self.current_floor:
            self.direction=Direction.UP
        else:
            self.direction=Direction.DOWN

        print(f"Elevator {self.elevator_id} moving to floor {floor}")

        self.current_floor=floor

        self.state=ElevatorState.IDLE
        self.direction=Direction.IDLE

    def open_door(self)->None:
        self.state=ElevatorState.DOOR_OPEN
        print(f"Elevator {self.elevator_id} door opened")

    def close_door(self)->None:
        self.state=ElevatorState.IDLE
        print(f"Elevator {self.elevator_id} door closed")
