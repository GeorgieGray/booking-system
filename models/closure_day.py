from sqlalchemy import Column, Integer, Date, ForeignKey, String
from .restaurant import Restaurant
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from db import base

class ClosureDay(base):
    __tablename__="closure_days"
    id = Column(Integer, primary_key=True)
    date = Column(Date)
    reason = Column(String)
    restaurant_id = Column(Integer, ForeignKey("restaurant_info.id"))