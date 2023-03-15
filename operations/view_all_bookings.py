import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.booking import Booking 
from db import session

def view_all_bookings(user_id: int):
    bookings = session.query(Booking).filter_by(user_id=user_id).all()
    return bookings
