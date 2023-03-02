from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db = create_engine("postgresql://wwwxcqyh:TBnbC6bNJ81AUkt_xtPJX96yCyTWCe_9@kandula.db.elephantsql.com/wwwxcqyh")
base = declarative_base()
Session = sessionmaker(db)
session = Session()
base.metadata.create_all(db)
