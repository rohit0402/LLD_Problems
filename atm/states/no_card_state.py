from interfaces.atm_state import AtmState

class NoCardState(AtmState):
    def insert_card(self,atm,card):
        atm.card = card
        print("Card inserted successfully.")

        from states.card_inserted_state import CardInsertedState
        atm.set_state(CardInsertedState())

    def enter_pin(self,atm,pin):
        raise ValueError("No card inserted.")

    def withdraw(self,atm,amount):
        raise ValueError("No card inserted.")

    def deposit(self,atm,amount):
        raise ValueError("No card inserted.")

    def check_balance(self,atm):
        raise ValueError("No card inserted.")

    def eject_card(self,atm):
        raise ValueError("No card inserted.")