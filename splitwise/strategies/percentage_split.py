from entities.split import Split

class PercentageSplit(Split):
    def __init__(self,percentages:dict):
        self.percentages=percentages

    def calculate(self,total_amount:float,participants:list)->dict:
        if set(self.percentages.keys()) != set(participants):
            raise ValueError("Participants and percentages don't match")

        total_percentage=sum(self.percentages.values())

        if total_percentage != 100:
            raise ValueError("Percentages don't add up to 100")

        return {user:total_amount*percentage/100 for user,percentage in self.percentages.items()}