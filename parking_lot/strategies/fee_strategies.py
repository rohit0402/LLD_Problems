from datetime import datetime
from interfaces.fee_strategy import FeeStrategy

def calculate_hours(entry_time:datetime, exit_time:datetime) -> int:
    seconds=(exit_time-entry_time).total_seconds()
    return max(1,int(seconds/3600))

class BikeFeeStrategy(FeeStrategy):
    def calculate_fee(self, entry_time, exit_time):
        return 20*calculate_hours(entry_time,exit_time)

class CarFeeStrategy(FeeStrategy):
    def calculate_fee(self, entry_time, exit_time):
        return 40*calculate_hours(entry_time,exit_time)

class TruckFeeStrategy(FeeStrategy):
    def calculate_fee(self, entry_time, exit_time):
        return 60*calculate_hours(entry_time,exit_time)