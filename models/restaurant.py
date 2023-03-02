from sqlalchemy import Column, Integer, String
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from db import base

class Restaurant(base):
    __tablename__="restaurant_info"
    id = Column(Integer, primary_key=True)
    table_time_limit = Column(Integer)
    phone_number = Column(String)
    name = Column(String)