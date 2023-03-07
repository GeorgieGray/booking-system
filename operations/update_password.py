import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.user import User
from db import session


def update_password(id: int, password: str):    
    session.query(User).filter_by(id=id).update({"password": password})
    return True

    