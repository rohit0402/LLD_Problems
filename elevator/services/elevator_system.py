class ElevatorSystem:
    def __init__(self,selector):
        self.selector=selector
        self.elevators=[]

    def add_elevator(self,elevator):
        self.elevators.append(elevator)

    def request_elevator(self,request):
        if not self.elevators:
            raise ValueError("No elevators available")

        elevator=self.selector.select_elevator(self.elevators,request)
        print(f"Elevator {elevator.elevator_id} selected")
        elevator.move_to(request.source_floor)
        elevator.open_door()
        return elevator