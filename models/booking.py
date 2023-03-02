from sqlalchemy import Column, Integer, Date, ForeignKey, String
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from db import base

class Booking(base):
    __tablename__="bookings"
    id = Column(Integer, primary_key=True)
    group_size = Column(Integer)
    time = Column(Integer)
    date = Column(Date)
    table_id = Column(Integer,ForeignKey("Table.id"))
    user_id = Column(Integer,ForeignKey("User.id"))
    note = Column(String)