from abc import ABC, abstractmethod

class AtmState(ABC):
    @abstractmethod
    def insert_card(self,atm,card):
        pass

    @abstractmethod
    def enter_pin(self,atm,pin):
        pass

    @abstractmethod
    def withdraw(self,atm,amount):
        pass


    @abstractmethod
    def deposit(self,atm,amount):
        pass
    
    @abstractmethod
    def check_balance(self,atm):
        pass

    @abstractmethod
    def eject_card(self,atm):
        pass
