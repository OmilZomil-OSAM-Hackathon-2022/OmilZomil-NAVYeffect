from sqlalchemy import create_engine
from app.core.settings import DB_INFO
from app.models.base_access import Base as base_access_model
from app.models.enlisted_personnel import Base as enlisted_personnel_model


db_url = "mysql+mysqldb://{user}:{pw}@{ip}:{port}/{name}".format(**DB_INFO)
engine = create_engine(db_url, echo=True)

base_access_model.metadata.create_all(bind=engine)
enlisted_personnel_model.metadata.create_all(bind=engine)
