from entities.expense import Expense

class ExpenseService:
    def __init__(self,balance_sheet):
        self.balance_sheet=balance_sheet
        self.expenses={}

    def add_expense(self,expense_id,amount,paid_by,participants,split):
        amounts=split.calculate(amount,participants)
        expense=Expense(expense_id,amount,paid_by,participants,split)
        self.expenses[expense_id]=expense
        for user,amount in amounts.items():
            self.balance_sheet.update_balance(paid_by,user,amount)
        return expense

