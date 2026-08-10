from interfaces.elevator_selection_strategy import ElevatorSelectionStrategy

class NearestElevatorStrategy(ElevatorSelectionStrategy):
    def select_elevator(self,elevators,request):
        return min(elevators,key=lambda elevator:abs(elevator.current_floor-request.source_floor))