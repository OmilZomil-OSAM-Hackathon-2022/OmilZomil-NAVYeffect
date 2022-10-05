from sqlalchemy import create_engine
from core.settings import DB_INFO
from app.user.model import Base as user_model
from app.camera.model import Base as camera_model
from app.base_access.model import Base as base_access_model
from app.enlisted_personnel.model import Base as enlisted_personnel_model


db_url = "mysql+mysqldb://{user}:{pw}@{ip}:{port}/{name}".format(**DB_INFO)

engine = create_engine(db_url, echo=True)
user_model.metadata.create_all(bind=engine)
camera_model.metadata.create_all(bind=engine)
base_access_model.metadata.create_all(bind=engine)
enlisted_personnel_model.metadata.create_all(bind=engine)
