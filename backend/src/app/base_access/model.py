from sqlalchemy import Column, Integer, String, DateTime, LargeBinary
from core.db import Base


class BaseAccess(Base):
    __tablename__ = "base_access"

    access_id = Column(Integer, primary_key=True, index=True)
    base_name = Column(String(30))  # 부대명
    access_time = Column(DateTime)  # 출입 시간
    image = Column(LargeBinary)  # 출입 사진
