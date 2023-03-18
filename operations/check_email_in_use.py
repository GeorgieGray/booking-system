import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.user import User 
from db import session

def check_email_in_use(email: str):
    count = session.query(User).filter_by(email=email).count()
    return count > 0
