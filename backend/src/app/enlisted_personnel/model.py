from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from core.db import Base


class EnlistedPersonnel(Base):
    __tablename__ = "enlisted_personnel"

    personnel_id = Column(Integer, primary_key=True, index=True, nullable=False)
    access_id = Column(Integer, ForeignKey("base_access.id"), nullable=False)
    army_type = Column(String(30), nullable=False)  # 군 구분
    name = Column(String(30), nullable=False)  # 이름
    rank = Column(String(30), nullable=False)  # 계급
    uniform_type = Column(String(30), nullable=False)  # 복장유형
    has_name = Column(Boolean, nullable=False)  # 이름표 부착 유무
    has_rank = Column(Boolean, nullable=False)  # 계급장 부착 유무
    has_neckerchief = Column(Boolean, nullable=False)  # 네커치프&네커치프링 착용 유무
    has_muffler = Column(Boolean, nullable=False)  # 머플러 착용 유무
    has_flag = Column(Boolean, nullable=False)  # 태극기 부착 유무
