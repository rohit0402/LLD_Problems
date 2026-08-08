from entities.parking_lot import ParkingLot
from entities.vehicle import Vehicle
from entities.ticket import Ticket
from factories.fee_strategy_factory import FeeStrategyFactory
from datetime import datetime
from services.fee_calculator import FeeCalculator
from services.payment_service import PaymentService


class ParkingService:
    def __init__(self,parking_lot:ParkingLot,fee_calculator:FeeCalculator, payment_service:PaymentService):
        self.fee_calculator = fee_calculator
        self.parking_lot=parking_lot
        self.payment_service = payment_service

    def park_vehicle(self,vehicle:Vehicle, ticket_id:str) -> Ticket:
        if self.parking_lot.is_vehicle_parked(vehicle.license_number):
            raise ValueError(f"Vehicle with license number {vehicle.license_number} is already parked")
        
        spot = self.parking_lot.find_available_spot(vehicle)
        if spot is None:
            raise ValueError(f"No spot available for vehicle of type {vehicle.vehicle_type}")


        spot.park_vehicle(vehicle)
        self.parking_lot.parked_vehicles.add(vehicle.license_number)        
        return Ticket(ticket_id, vehicle, spot)

    def unpark_vehicle(self, ticket):

        if ticket.exit_time is not None:
            raise ValueError(
                "Vehicle has already exited"
            )

        exit_time = datetime.now()

        strategy = FeeStrategyFactory.get_strategy(
            ticket.vehicle.vehicle_type
        )

        fee = self.fee_calculator.calculate(
            strategy,
            ticket.entry_time,
            exit_time
        )

        if not self.payment_service.process_payment(fee):
            raise ValueError(
                "Payment failed. Vehicle remains parked."
            )

        ticket.exit_time = exit_time

        ticket.spot.remove_vehicle()

        self.parking_lot.remove_vehicle(
            ticket.vehicle.license_number
        )

        return fee