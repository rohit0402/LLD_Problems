from datetime import datetime
from enums.parking_enums import PaymentMethod, PaymentStatus

class Payment:
    def __init__(self,payment_id:str, payment_method:PaymentMethod, amount:float, status:PaymentStatus):
        self.payment_id = payment_id
        self.payment_method = payment_method
        self.amount = amount
        self.status = status
        self.payment_time = datetime.now()  