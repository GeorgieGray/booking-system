import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.user import User 
from db import session

def get_user(email: str):
    user = session.query(User).filter_by(email=email).one()
    return user
