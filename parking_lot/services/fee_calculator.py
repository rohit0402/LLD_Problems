from interfaces.fee_strategy import FeeStrategy


class FeeCalculator:

    def calculate(
        self,
        strategy: FeeStrategy,
        entry_time,
        exit_time
    ) -> float:

        return strategy.calculate_fee(
            entry_time,
            exit_time
        )