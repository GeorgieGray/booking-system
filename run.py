from db import session
from models.booking import Booking
import datetime

bookings = session.query(Booking)
for booking in bookings:
    print(booking.group_size, booking.date, sep = " | ")

booking = Booking(group_size = 2, time = 2, date = datetime.datetime.now(), note = "hello world", table_id=1, user_id=1)

session.add(booking)

session.commit()