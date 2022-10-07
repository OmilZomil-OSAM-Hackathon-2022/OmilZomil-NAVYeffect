from sqlalchemy import Column, Integer, String, DateTime, LargeBinary
from app.db.base_schema import Base


class AccessLog(Base):
    __tablename__ = "access_log"

    access_id = Column(Integer, primary_key=True, index=True, nullable=False)
    military_base = Column(String(30), nullable=False)
    access_time = Column(DateTime, nullable=False)
    image = Column(LargeBinary, nullable=False)
