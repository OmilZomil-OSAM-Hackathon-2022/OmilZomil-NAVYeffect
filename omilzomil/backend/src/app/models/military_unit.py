from sqlalchemy import Column, Integer, String
from app.db.base_schema import Base


class MilitaryUnit(Base):
    __tablename__ = "military_unit"

    unit_id = Column(Integer, primary_key=True, index=True)
    unit = Column(String(128), unique=True, nullable=False)
