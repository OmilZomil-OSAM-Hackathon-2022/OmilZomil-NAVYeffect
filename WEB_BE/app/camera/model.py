from sqlalchemy import Boolean, Column, String, Text, Integer

from core.db import Base

class Camera(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)   # 성명
    pos = Column(String)