class OrderItem:
    def __init__(self,menu_item,quantity:int):
        if quantity<1:
            raise ValueError("Quantity cannot be less than 1")

        self.menu_item=menu_item
        self.quantity=quantity

    def get_total(self)->float:
        return self.quantity*self.menu_item.price