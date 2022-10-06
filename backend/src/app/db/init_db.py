from sqlalchemy.orm import Session
from app.db.session import engine
from app.models.base_access import Base as base_access_model
from app.models.enlisted_personnel import Base as enlisted_personnel_model


def init_db(db: Session):
    base_access_model.metadata.create_all(bind=engine)
    enlisted_personnel_model.metadata.create_all(bind=engine)
