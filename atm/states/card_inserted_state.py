from interfaces.atm_state import AtmState

class CardInsertedState(AtmState):
    def insert_card(self,atm,card):
        raise ValueError("Card already inserted.")

    def enter_pin(self,atm,pin):
        if atm.card.validate_pin(pin):
            print("PIN entered successfully.")
            from states.authenticated_state import AuthenticatedState
            atm.set_state(AuthenticatedState())
        else:
            raise ValueError("Invalid PIN.")

    def withdraw(self,atm,amount):
        raise ValueError("Enter PIN first.")

    def deposit(self,atm,amount):
        raise ValueError("Enter PIN first.")
    
    def check_balance(self,atm):
        raise ValueError("Enter PIN first.")

    def eject_card(self,atm):
        atm.card = None
        print("Card ejected successfully.")
        from states.no_card_state import NoCardState
        atm.set_state(NoCardState())

    