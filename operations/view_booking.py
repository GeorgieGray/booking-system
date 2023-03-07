import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.booking import Booking 
from db import session

def view_booking(id: int):
    booking = session.query(Booking).filter_by(id=id).one()
    return booking
