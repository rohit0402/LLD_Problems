from enum import Enum

class TransactionType(Enum):
    WITHDRAW = "WITHDRAW"
    DEPOSIT = "DEPOSIT"
    CHECK_BALANCE = "CHECK_BALANCE"