from datetime import datetime

class InventoryTransaction:
    def __init__(self,transactioin_id:str,transaction_type:str,product,warehouse,quantity:int):
        self.transaction_id=transactioin_id
        self.transaction_type=transaction_type
        self.product=product
        self.warehouse=warehouse
        self.quantity=quantity
        self.timestamp=datetime.now()
        