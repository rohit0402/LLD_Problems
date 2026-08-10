from abc import ABC,abstractmethod

class ElevatorSelectionStrategy(ABC):
    @abstractmethod
    def select_elevator(self,elevators,request):
        pass