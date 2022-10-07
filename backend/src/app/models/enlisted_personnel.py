from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from app.db.base_schema import Base


class EnlistedPersonnel(Base):
    __tablename__ = "enlisted_personnel"

    personnel_id = Column(Integer, primary_key=True, index=True, nullable=False)
    access_id = Column(Integer, ForeignKey("base_access.access_id"), nullable=False)
    army_type = Column(String(30), nullable=False)
    name = Column(String(30), nullable=False)
    rank = Column(String(30), nullable=False)
    uniform_type = Column(String(30), nullable=False)
    has_name = Column(Boolean, nullable=False)
    has_rank = Column(Boolean, nullable=False)
    has_neckerchief = Column(Boolean, nullable=False)
    has_muffler = Column(Boolean, nullable=False)
    has_flag = Column(Boolean, nullable=False)
