from sqlalchemy import Column, Integer, Boolean, ForeignKey
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from db import base

class TradingDay(base):
    __tablename__="trading_days"
    id = Column(Integer, primary_key=True)
    day = Column(Integer)
    restaurant_id = Column(Integer, ForeignKey("Restaurant.id"))
    opening_time = Column(Integer)
    closing_time = Column(Integer)
    is_open = Column(Boolean)
    

   