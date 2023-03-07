from sqlalchemy import Column, Integer, String
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from db import base

class User(base):
    __tablename__="users"
    id = Column(Integer, primary_key=True)
    email = Column(String)
    password = Column(String)
    phone_number = Column(String)
    first_name = Column(String)
    last_name = Column(String)
   