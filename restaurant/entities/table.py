from enums.restaurant_enum import TableStatus

class Table:
    def __init__(self,table_id:str,capacity:int):
        self.table_id=table_id
        self.capacity=capacity
        self.status=TableStatus.AVAILABLE

    def reserve(self):
        if self.status!=TableStatus.AVAILABLE:
            raise ValueError("Table is not available")

        self.status=TableStatus.RESERVED

    def occupy(self):
        if self.status not in (TableStatus.RESERVED,TableStatus.AVAILABLE):
            raise ValueError("Table cannot be occupied")

        self.status=TableStatus.OCCUPIED

    def release(self)->None:
        self.status=TableStatus.AVAILABLE

    def is_available(self)->bool:
        return self.status==TableStatus.AVAILABLE