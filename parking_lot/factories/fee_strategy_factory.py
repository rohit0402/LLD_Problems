from enums.parking_enums import VehicleType
from interfaces.fee_strategy import FeeStrategy
from strategies.fee_strategies import (
    BikeFeeStrategy,
    CarFeeStrategy,
    TruckFeeStrategy,
)


class FeeStrategyFactory:

    @staticmethod
    def get_strategy(vehicle_type: VehicleType) -> FeeStrategy:

        if vehicle_type == VehicleType.BIKE:
            return BikeFeeStrategy()

        if vehicle_type == VehicleType.CAR:
            return CarFeeStrategy()

        if vehicle_type == VehicleType.TRUCK:
            return TruckFeeStrategy()

        raise ValueError(
            f"Unsupported vehicle type: {vehicle_type}"
        )