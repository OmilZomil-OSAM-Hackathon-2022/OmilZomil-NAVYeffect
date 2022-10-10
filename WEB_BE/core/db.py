
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from core.settings import DB_INFO

db_url = 'postgresql://{user}:{pw}@{ip}:{port}/{name}'.format(**DB_INFO)
engine = create_engine(db_url)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()

def get_db():
    db = db_session()
    try:
        yield db
    finally:
        db.close()