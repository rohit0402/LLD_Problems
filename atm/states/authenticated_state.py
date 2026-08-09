from interfaces.atm_state import AtmState

class AuthenticatedState(AtmState):
    def insert_card(self,atm,card):
        raise ValueError("Authenticated state.")

    def enter_pin(self,atm,pin):
        raise ValueError("Authenticated state.")

    def withdraw(self,atm,amount):
        if amount<=0:
            raise ValueError("Amount must be positive.")

        if amount>atm.card.account.get_balance():
            raise ValueError("Insufficient balance.")

        if amount>atm.cash:
            raise ValueError("Insufficient cash.")


        atm.card.account.withdraw(amount)
        atm.cash-=amount
        print(f"Withdrawn {amount} from account {atm.card.account.account_number}.")
        print(f"Cash balance: {atm.cash}")

    def deposit(self,atm,amount):
        if amount<=0:
            raise ValueError("Amount must be positive.")

        atm.card.account.deposit(amount)
        atm.cash+=amount
        print(f"Deposited {amount} to account {atm.card.account.account_number}.")
        print(f"Cash balance: {atm.cash}")

    def check_balance(self,atm):
        balance = atm.card.account.get_balance()
        print(f"Account balance: {balance}")
        return balance

    def eject_card(self,atm):
        atm.card = None
        print("Card ejected successfully.")
        from states.no_card_state import NoCardState    
        atm.set_state(NoCardState())