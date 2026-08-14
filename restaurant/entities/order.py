from enums.restaurant_enum import OrderStatus
from entities.order_item import OrderItem
class Order:
    def __init__(self,order_id:str,table):
        self.order_id=order_id
        self.table=table
        self.items=[]
        self.status=OrderStatus.CREATED

    def add_item(self,menu_item,quantity:int):
        from entities.order_item import OrderItem
        item=OrderItem(menu_item,quantity)
        self.items.append(item)

    def get_subtotal(self)->float:
        return sum([item.get_total() for item in self.items])

    def update_status(self,status:OrderStatus):
        self.status=status