from datetime import datetime
class Reservation:
    def __init__(self,reservation_id:str,customer_id:str,table_id:str,reservation_time:datetime):
        self.reservation_id=reservation_id
        self.customer_id=customer_id
        self.table_id=table_id
        self.reservation_time=reservation_time