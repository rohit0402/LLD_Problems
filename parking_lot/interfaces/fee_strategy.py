from abc import ABC, abstractmethod
from datetime import datetime

# @abstractmethod used because we want to create a base class for fee calculation strategy and we want to
#  force the subclasses to implement the calculate_fee method
class FeeStrategy(ABC):
    @abstractmethod
    def calculate_fee(self, entry_time:datetime, exit_time:datetime) -> float:
        pass

# it saying every fee strategy must know how to calculate fee.
