from datetime import datetime
from sqlalchemy import Column, Integer, DateTime, ForeignKey
from app.db.base_schema import Base
from app.models.military_unit import MilitaryUnit


class AccessLog(Base):
    __tablename__ = "access_log"

    access_id = Column(Integer, primary_key=True, index=True)
    military_unit = Column(Integer, ForeignKey(MilitaryUnit.unit_id), nullable=False)
    access_time = Column(DateTime, default=datetime.now())
