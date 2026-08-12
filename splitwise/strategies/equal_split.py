from entities.split import Split


class EqualSplit(Split):

    def calculate(
        self,
        total_amount: float,
        participants: list
    ) -> dict:

        if not participants:
            raise ValueError("No participants")

        share = total_amount / len(participants)

        return {
            user: share
            for user in participants
        }