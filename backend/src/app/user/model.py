from sqlalchemy import Boolean, Column, String, Text, Integer

from core.db import Base

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(30))   # 성명
    uid = Column(String(50))
    password = Column(String(300))
    army = Column(String(50))  # 육해공군
    unit = Column(String(50))   # 소속
    dog_num = Column(String(50)) # 군번
    rank = Column(String(50))    # 계급
    permission = Column(Integer)# 권한