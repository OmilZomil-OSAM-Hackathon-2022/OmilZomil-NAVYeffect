from sqlalchemy import Column, Integer, DateTime, String, ForeignKey
from app.db.base_schema import Base
from app.models.military_unit import MilitaryUnit


class AccessLog(Base):
    __tablename__ = "access_log"

    access_id = Column(Integer, primary_key=True, index=True)
    military_unit = Column(Integer, ForeignKey(MilitaryUnit.unit_id), nullable=False)
    access_time = Column(DateTime, nullable=False)
    image_path = Column(String(1024), nullable=False)
