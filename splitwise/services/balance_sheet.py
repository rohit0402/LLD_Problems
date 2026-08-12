from collections import defaultdict

class BalanceSheet:
    def __init__(self):
        self.balances=defaultdict(lambda:defaultdict(float))


    def update_balance(self,paid_by,user,amount):
        if paid_by == user:
            return 

        self.balances[paid_by][user]+=amount

    def get_balance(self,user1,user2):
        return self.balances[user1][user2]

    def show_balances(self):
        for user, creditors in self.balances.items():
            for creditor, amount in creditors.items():
                if amount > 0:
                    print(f"{user.name} owes {creditor.name}: ${amount:.2f}")

    def settle(self,debtor,creditor,amount):
        current=self.balances[debtor][creditor]
        if amount>current:
            raise ValueError("Not enough money")

        self.balances[debtor][creditor]-=amount