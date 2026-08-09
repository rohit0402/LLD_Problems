class Account:
    def __init__(self,account_number:str,balance:float):
        self.account_number = account_number
        self.balance = balance

    def deposit(self,amount:float)->None:
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        self.balance += amount

    def withdraw(self,amount:float)->None:
        if amount <= 0:
            raise ValueError("Amount must be positive.")

        if self.balance < amount:
            raise ValueError("Insufficient balance.")

        self.balance -= amount

    def get_balance(self)->float:
        return self.balance