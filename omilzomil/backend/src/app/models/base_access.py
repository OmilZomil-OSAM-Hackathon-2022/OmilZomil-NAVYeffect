from sqlalchemy import Column, Integer, String, DateTime, LargeBinary
from app.db.base_schema import Base


class BaseAccess(Base):
    __tablename__ = "base_access"

    access_id = Column(Integer, primary_key=True, index=True, nullable=False)
    base_name = Column(String(30), nullable=False)  # 부대명
    access_time = Column(DateTime, nullable=False)  # 출입 시간
    image = Column(LargeBinary, nullable=False)  # 출입 사진
