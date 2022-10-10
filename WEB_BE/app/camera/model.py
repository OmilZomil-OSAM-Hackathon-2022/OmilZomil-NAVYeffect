from sqlalchemy import Boolean, Column, String, Text, Integer

from core.db import Base

class Camera(Base):
    __tablename__ = 'camera'

    id = Column(Integer, primary_key=True, index=True)
    uid = Column(String, unique=True)
    name = Column(String)   # 성명
    pos = Column(String)