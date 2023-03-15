import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.booking import Booking 
from db import session

def view_booking(id: int, user_id: int):
    booking = session.query(Booking).filter_by(id=id,user_id=user_id).one()
    return booking
