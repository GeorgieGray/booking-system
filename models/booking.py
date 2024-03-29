from sqlalchemy import Column, Integer, Date, ForeignKey, String, inspect
from sqlalchemy.orm import relationship

from .table import Table
from .user import User
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from db import base

class Booking(base):
    __tablename__="bookings"
    id = Column(Integer, primary_key=True)
    group_size = Column(Integer)
    time = Column(Integer)
    date = Column(Date)
    table_id = Column(Integer,ForeignKey("tables.id"))
    user_id = Column(Integer,ForeignKey("users.id"))
    note = Column(String)
    table = relationship("Table", foreign_keys=[table_id], viewonly=True)

    def toDict(self):
        # https://stackoverflow.com/a/46180522
        return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }