class Bill:
    def __init__(self,order,tax_rate:float = 0.05):
        self.order=order
        self.subtotal=order.get_subtotal()
        self.tax=self.subtotal*tax_rate
        self.total=self.subtotal+self.tax