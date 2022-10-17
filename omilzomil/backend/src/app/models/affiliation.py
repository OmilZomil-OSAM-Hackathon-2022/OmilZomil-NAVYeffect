from sqlalchemy import Column, Integer, String
from app.db.base_schema import Base


class Affiliation(Base):
    __tablename__ = "affiliation"

    affiliation_id = Column(Integer, primary_key=True, index=True)
    affiliation = Column(String(6), unique=True, nullable=False)
