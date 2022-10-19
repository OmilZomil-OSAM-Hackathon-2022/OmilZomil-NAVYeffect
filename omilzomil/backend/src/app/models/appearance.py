from sqlalchemy import Column, Integer, String
from app.db.base_schema import Base


class Appearance(Base):
    __tablename__ = "appearance"

    appearance_id = Column(Integer, primary_key=True, index=True)
    appearance = Column(String(12), unique=True, nullable=False)
