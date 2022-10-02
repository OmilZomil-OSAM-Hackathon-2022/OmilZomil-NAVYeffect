from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from core.settings import DB_INFO

db_url = 'mysql+mysqldb://{user}:{pw}@{ip}:{port}:{name}'.format(**DB_INFO)
print(db_url)

engine = create_engine(db_url, echo=True)


from app.user.model import Base as user_model
from app.camera.model import Base as camera_model

user_model.metadata.create_all(bind=engine)
camera_model.metadata.create_all(bind=engine)
