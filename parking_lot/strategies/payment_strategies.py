from interfaces.payment_strategy import PaymentStrategy

#following OCP
class CashPaymentStrategy(PaymentStrategy):
    def pay(self, amount:float) -> bool:
        print(f"Paid ₹{amount} using Cash")
        return True

class CardPaymentStrategy(PaymentStrategy):
    def pay(self, amount:float) -> bool:
        print(f"Paid ₹{amount} using Card") 
        return True