from sqlalchemy import Column, Integer, String
from app.db.base_schema import Base


class Guardhouse(Base):
    __tablename__ = "guardhouse"

    house_id = Column(Integer, primary_key=True, index=True)
    house = Column(String(128), unique=True, nullable=False)
