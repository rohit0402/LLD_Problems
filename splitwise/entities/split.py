from abc import ABC,abstractmethod

class Split(ABC):
    
    
    @abstractmethod
    def calculate(self,total_amount:float,participants:list)->dict:
        pass