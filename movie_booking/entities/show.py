class Show:
    def __init__(self,show_id:str,movie,screen,start_time):
        self.show_id=show_id
        self.movie=movie
        self.screen=screen
        self.start_time=start_time
        self.booked_seats=set()


    def is_seat_available(self,seat_id:str)->bool:
        return seat_id not in self.booked_seats

    def book_seat(self,seat_id:str)->None:
        if not self.is_seat_available(seat_id):
            raise ValueError(f"Seat{seat_id} is already booked")

        self.booked_seats.add(seat_id)

    def cancel_seat(self,seat_id:str)->None:
        if seat_id not in self.booked_seats:
            raise ValueError(f"Seat{seat_id} is not booked")

        self.booked_seats.remove(seat_id)