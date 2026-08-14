class InventoryItem:
    def __init__(self,product,warehouse):
        self.product=product
        self.warehouse=warehouse
        self.available_quantity=0
        self.reserved_quantity=0

    @property
    def total_quantity(self):
        return self.available_quantity+self.reserved_quantity

    def add_stock(self,quantity:int):
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        self.available_quantity+=quantity


    def remove_stock(self,quantity:int):
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        if quantity > self.available_quantity:
            raise ValueError("Quantity cannot be greater than available quantity")


        self.available_quantity-=quantity

    def reserve(self,quantity:int):
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        if quantity > self.available_quantity:
            raise ValueError("Quantity cannot be greater than available quantity")

        self.available_quantity-=quantity
        self.reserved_quantity+=quantity

    def release(self,quantity:int):
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        if quantity > self.available_quantity:
            raise ValueError("Quantity cannot be greater than available quantity")

        self.available_quantity-=quantity
        self.reserved_quantity+=quantity

    def sell_reserved(self,quantity:int):
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        if quantity > self.reserved_quantity:
            raise ValueError("Quantity cannot be greater than reserved quantity")

        self.reserved_quantity-=quantity