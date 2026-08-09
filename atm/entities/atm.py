from states.no_card_state import NoCardState



class ATM:
    def __init__(self,cash:float):
        self.cash = cash
        self.card = None
        self.state = NoCardState()


    def set_state(self,state):
        self.state = state

    def insert_card(self,card):
        self.state.insert_card(self,card)

    def enter_pin(self,pin):
        self.state.enter_pin(self,pin)

    def withdraw(self,amount):
        self.state.withdraw(self,amount)

    def deposit(self,amount):
        self.state.deposit(self,amount)

    def check_balance(self):
        return self.state.check_balance(self)

    def eject_card(self):
        self.state.eject_card(self)