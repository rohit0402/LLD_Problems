from datetime import datetime

from entities.user import User
from entities.movie import Movie
from entities.seat import Seat
from entities.screen import Screen
from entities.theatre import Theatre
from entities.show import Show

from services.booking_service import BookingService


# -----------------------------------------
# User
# -----------------------------------------

user = User(
    "U1",
    "Rohit"
)


# -----------------------------------------
# Movie
# -----------------------------------------

movie = Movie(
    "M1",
    "Interstellar",
    169
)


# -----------------------------------------
# Seats
# -----------------------------------------

seat1 = Seat("A1", "A", 1)
seat2 = Seat("A2", "A", 2)
seat3 = Seat("A3", "A", 3)


# -----------------------------------------
# Screen
# -----------------------------------------

screen = Screen("S1")

screen.add_seat(seat1)
screen.add_seat(seat2)
screen.add_seat(seat3)


# -----------------------------------------
# Theatre
# -----------------------------------------

theatre = Theatre(
    "T1",
    "PVR"
)

theatre.add_screen(screen)


# -----------------------------------------
# Show
# -----------------------------------------

show = Show(
    "SH1",
    movie,
    screen,
    datetime.now()
)


# -----------------------------------------
# Booking Service
# -----------------------------------------

booking_service = BookingService()

booking_service.add_show(show)


# -----------------------------------------
# Available Seats
# -----------------------------------------

available = (
    booking_service
    .get_available_seats("SH1")
)

print("Available seats:")

for seat in available:
    print(seat.seat_id)


# -----------------------------------------
# Book Seats
# -----------------------------------------

booking = (
    booking_service.book_seats(
        "B1",
        user,
        "SH1",
        ["A1", "A2"]
    )
)

print(
    f"Booking {booking.booking_id} "
    f"confirmed"
)


# -----------------------------------------
# Available After Booking
# -----------------------------------------

available = (
    booking_service
    .get_available_seats("SH1")
)

print("Available seats after booking:")

for seat in available:
    print(seat.seat_id)


# -----------------------------------------
# Cancel Booking
# -----------------------------------------

booking_service.cancel_booking(
    "B1"
)

print("Booking cancelled")


# -----------------------------------------
# Available After Cancellation
# -----------------------------------------

available = (
    booking_service
    .get_available_seats("SH1")
)

print("Available seats after cancellation:")

for seat in available:
    print(seat.seat_id)