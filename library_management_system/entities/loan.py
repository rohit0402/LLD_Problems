from datetime import datetime, timedelta

class Loan:
    def __init__(self,loan_id:str,member,book_copy):
        self.loan_id = loan_id
        self.member = member
        self.book_copy = book_copy
        self.issue_date = datetime.now()
        self.due_date = self.issue_date + timedelta(days=14) 
        self.return_date = None

    def close(self)->None:
        if self.return_date is not None:
            raise Exception("Loan is already closed.")
        self.return_date = datetime.now()