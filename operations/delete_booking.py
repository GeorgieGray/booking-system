import os, sys
from .view_booking import view_booking
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.booking import Booking 
from db import session

def delete_booking(id: int):
    booking = session.query(Booking).filter_by(id=id)
    booking.delete()
    return True