from enums.elevator_enums import Direction

class ElevatorRequest:
    def __init__(self,source_floor:int,direction:Direction):
        self.source_floor=source_floor
        self.direction=direction