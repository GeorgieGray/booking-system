import os, sys, datetime
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.booking import Booking 
from db import session

def create_booking(group_size: int, table_id: int, time: int, date: datetime, user_id: int, note: str):
    booking = Booking(group_size=group_size,table_id=table_id,time=time,date=date,user_id=user_id,note=note)
    session.add(booking)
    session.commit()