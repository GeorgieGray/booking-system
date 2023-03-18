import re
 
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

def is_valid_email(email):
    if(re.fullmatch(regex, email)):
        return True
    else:
        return False

def length_between(value: str, min: int, max: int):
    return len(value) >= min and len(value) <= max