from sqlalchemy import Column, Integer, String, DateTime, LargeBinary
from app.db.base_schema import Base


class BaseAccess(Base):
    __tablename__ = "base_access"

    access_id = Column(Integer, primary_key=True, index=True, nullable=False)
    base_name = Column(String(30), nullable=False)
    access_time = Column(DateTime, nullable=False)
    image = Column(LargeBinary, nullable=False)
