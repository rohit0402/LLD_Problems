from entities.split import Split


class ExactSplit(Split):

    def __init__(self, amounts: dict):
        self.amounts = amounts

    def calculate(
        self,
        total_amount: float,
        participants: list
    ) -> dict:

        if set(self.amounts.keys()) != set(participants):
            raise ValueError(
                "Participants and amounts don't match"
            )

        if sum(self.amounts.values()) != total_amount:
            raise ValueError(
                "Total amount and amounts don't match"
            )

        return self.amounts