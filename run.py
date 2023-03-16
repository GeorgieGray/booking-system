import jsonpickle

# from db import session
# from models.booking import Booking
from operations.view_booking import view_booking 
# import datetime
from operations.view_all_bookings import view_all_bookings
from operations.create_booking import create_booking 
from operations.view_available_times import view_available_times
import datetime


# bookings = session.query(Booking)
# for booking in bookings:
#     print(booking.group_size, booking.date, sep = " | ")

# booking = Booking(group_size = 2, time = 2, date = datetime.datetime.now(), note = "hello world", table_id=1, user_id=1)

# session.add(booking)

# session.commit()
# booking=view_booking(15)
# json = jsonpickle.encode(booking)
# print(json)
# bookings = view_all_bookings(0)
# for booking in bookings: 
#     print(booking.id)
# date = datetime.datetime(2023, 5, 17)
today = datetime.datetime.today()
view_available_times(restaurant_id=2, group_size=2, booking_day=today)
# create_booking(table_id= 3, group_size= 2, time = 11, date = today, user_id = 1, note = "lol")
# create_booking(table_id= 4, group_size= 2, time = 11, date = today, user_id = 1, note = "lol")
# create_booking(table_id= 5, group_size= 2, time = 11, date = today, user_id = 1, note = "lol")
# create_booking(table_id= 6, group_size= 2, time = 11, date = today, user_id = 1, note = "lol")
# create_booking(table_id= 7, group_size= 2, time = 11, date = today, user_id = 1, note = "lol")
# create_booking(table_id= 8, group_size= 2, time = 11, date = today, user_id = 1, note = "lol")
# create_booking(table_id= 9, group_size= 2, time = 11, date = today, user_id = 1, note = "lol")



