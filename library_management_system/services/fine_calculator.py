from datetime import datetime

class FineCalculator:
    def __init__(self,rate_per_day:float):
        self.rate_per_day = rate_per_day

    def calculate(self,due_date:datetime,return_date:datetime)->float:
        if return_date<=due_date:
            return 0.0
        days_overdue=(return_date-due_date).days
        fine = days_overdue*self.rate_per_day
        return fine