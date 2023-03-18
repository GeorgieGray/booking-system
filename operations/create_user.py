import os, sys, datetime
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.user import User 
from db import session

def create_user(email: str, password: str, first_name: str, last_name: str):
    user = User(email=email, password=password, first_name=first_name, last_name=last_name)
    session.add(user)
    session.commit()
    return user