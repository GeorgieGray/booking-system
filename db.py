import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()
DB_URL = os.getenv('DB_URL')
db = create_engine(DB_URL)
base = declarative_base()
Session = sessionmaker(db)
session = Session()
base.metadata.create_all(db)
