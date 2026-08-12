from entities.user import User
from entities.group import Group

from strategies.equal_split import EqualSplit
from strategies.exact_split import ExactSplit
from strategies.percentage_split import PercentageSplit

from services.balance_sheet import BalanceSheet
from services.expense_service import ExpenseService


# Users

rohit = User("U1", "Rohit")
amit = User("U2", "Amit")
rahul = User("U3", "Rahul")


# Group

group = Group(
    "G1",
    "Trip"
)

group.add_member(rohit)
group.add_member(amit)
group.add_member(rahul)


# Services

balance_sheet = BalanceSheet()

expense_service = ExpenseService(
    balance_sheet
)


# ------------------------------------------------
# Equal Split
# ------------------------------------------------

expense_service.add_expense(
    "E1",
    900,
    rohit,
    [rohit, amit, rahul],
    EqualSplit()
)


balance_sheet.show_balances()


# ------------------------------------------------
# Exact Split
# ------------------------------------------------

expense_service.add_expense(
    "E2",
    600,
    amit,
    [rohit, amit, rahul],
    ExactSplit({
        rohit: 200,
        amit: 200,
        rahul: 200
    })
)


balance_sheet.show_balances()


# ------------------------------------------------
# Percentage Split
# ------------------------------------------------

expense_service.add_expense(
    "E3",
    1000,
    rahul,
    [rohit, amit, rahul],
    PercentageSplit({
        rohit: 50,
        amit: 30,
        rahul: 20
    })
)


balance_sheet.show_balances()