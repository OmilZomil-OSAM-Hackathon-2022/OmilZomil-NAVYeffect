from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from app.db.base_schema import Base
from app.models.access_log import AccessLog
from app.models.uniform import Uniform


class InspectionLog(Base):
    __tablename__ = "inspection_log"

    inspection_id = Column(Integer, primary_key=True, index=True, nullable=False)
    access_id = Column(Integer, ForeignKey(AccessLog.access_id), nullable=False)
    affiliation = Column(String(6), nullable=False)
    name = Column(String(8), nullable=False)
    rank = Column(String(4), nullable=False)
    uniform = Column(String(3), ForeignKey(Uniform.uniform), nullable=False)
    has_name = Column(Boolean, nullable=False)
    has_rank = Column(Boolean, nullable=False)
    has_neckerchief = Column(Boolean, nullable=False)
    has_muffler = Column(Boolean, nullable=False)
    has_flag = Column(Boolean, nullable=False)
