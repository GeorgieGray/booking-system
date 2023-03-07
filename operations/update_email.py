import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.user import User
from db import session


def update_email(id: int, email: str):    
    exists = session.query(User).filter_by(email=email).count() >= 1
    if exists == True: 
        return False

    session.query(User).filter_by(id=id).update({"email": email})
    return True
    

    