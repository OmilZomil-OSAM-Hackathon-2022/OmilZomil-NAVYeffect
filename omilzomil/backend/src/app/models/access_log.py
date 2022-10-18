from datetime import datetime
from sqlalchemy import Column, Integer, DateTime, ForeignKey
from app.db.base_schema import Base
from app.models.guardhouse import Guardhouse


class AccessLog(Base):
    __tablename__ = "access_log"

    access_id = Column(Integer, primary_key=True, index=True)
    guardhouse = Column(Integer, ForeignKey(Guardhouse.house_id), nullable=False)
    access_time = Column(DateTime, default=datetime.now())
