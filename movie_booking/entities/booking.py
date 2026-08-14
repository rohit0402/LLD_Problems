from enums.booking_enums import BookingStatus

class Booking:
    def __init__(self,booking_id:str,user,show,seats):
        self.booking_id=booking_id
        self.user=user
        self.show=show
        self.seats=seats

        self.status=BookingStatus.CONFIRMED

    def cancel(self):
        if self.status == BookingStatus.CANCELLED:
            raise ValueError("Booking is already cancelled")

        for seat in self.seats:
            self.show.cancel_seat(seat.seat_id)

        self.status=BookingStatus.CANCELLED