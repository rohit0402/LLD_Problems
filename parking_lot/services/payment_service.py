from interfaces.payment_strategy import PaymentStrategy

class PaymentService:
    def __init__(self, strategy:PaymentStrategy):
        self.strategy = strategy

    def process_payment(self, amount:float) -> bool:
        return self.strategy.pay(amount)