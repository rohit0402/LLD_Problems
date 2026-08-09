from datetime import datetime
from enums.atm_enums import TransactionType

class Transaction:
    def __init__(self,transaction_id:str,transaction_type:TransactionType,amount:float=0,):
        self.transaction_type = transaction_type
        self.amount = amount
        self.timestamp = datetime.now()
        