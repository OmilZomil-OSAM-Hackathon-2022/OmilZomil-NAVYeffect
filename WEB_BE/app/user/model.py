from sqlalchemy import Boolean, Column, String, Text, Integer

from core.db import Base

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)   # 성명
    uid = Column(String)
    password = Column(String)
    army = Column(String)  # 육해공군
    unit = Column(String)   # 소속
    dog_num = Column(String) # 군번
    rank = Column(String)    # 계급
    permission = Column(Integer)# 권한