from sqlalchemy import Column, Integer, ForeignKey
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from db import base

class Table(base):
    __tablename__="tables"
    id = Column(Integer, primary_key=True)
    max_seats = Column(Integer)
    min_seats = Column(Integer)
    table_number = Column(Integer)
    restaurant_id = Column(Integer, ForeignKey("restaurant_info.id"))

   