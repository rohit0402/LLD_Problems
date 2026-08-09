class Card:
    def __init__(self,card_number:str,pin:str,account):
        self.card_number = card_number
        self.pin = pin
        self.account = account

    def validate_pin(self,pin:str)->bool:
        return self.pin == pin