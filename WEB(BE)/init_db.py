from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from core.settings import DB_INFO

db_url = 'postgresql://{user}:{pw}@{ip}:{port}/{name}'.format(**DB_INFO)
engine = create_engine(db_url, echo=True)


from app.user.model import Base as user_model

user_model.metadata.create_all(bind=engine)
