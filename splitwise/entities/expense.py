class Expense:
    def __init__(self,expense_id:str,amount:float,paid_by,participants:list,split):
        self.expense_id=expense_id
        self.amount=amount
        self.paid_by=paid_by
        self.participants=participants  
        self.split=split    
        