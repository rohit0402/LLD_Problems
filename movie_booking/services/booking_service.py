from entities.booking import Booking

class BookingService:
    def __init__(self):
        self.shows={}
        self.bookings={}

    def add_show(self,show):
        self.shows[show.show_id]=show

    def get_available_seats(self,show_id:str):
        if show_id not in self.shows:
            raise ValueError("Show not found")

        show=self.shows[show_id]

        return [seat for seat in show.screen.seats if show.is_seat_available(seat.seat_id)]

    def book_seats(self,booking_id,user,show_id,seat_ids):
        if show_id not in self.shows:
            raise ValueError("show not found")

        show=self.shows[show_id]

        if not seat_ids:
            raise ValueError("atleast one seat is required")

        screen_seat_map={seat.seat_id:seat for seat in show.screen.seats}

        for seat_id in seat_ids:
            if seat_id not in screen_seat_map:
                raise ValueError("seat not found")

            if not show.is_seat_available(seat_id):
                raise ValueError("seat is not available")

        selected_seats=[]

        for seat_id in seat_ids:
            show.book_seat(seat_id)
            selected_seats.append(screen_seat_map[seat_id])
            booking=Booking(booking_id,user,show,selected_seats)
            self.bookings[booking_id]=booking
            return booking

    def cancel_booking(self,booking_id):
        if booking_id not in self.bookings:
            raise ValueError("booking not found")

        booking=self.bookings[booking_id]
        booking.cancel()
