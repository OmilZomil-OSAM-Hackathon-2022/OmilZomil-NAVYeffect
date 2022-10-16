from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from app.db.base_schema import Base
from app.models.access_log import AccessLog
from app.models.affiliation import Affiliation
from app.models.rank import Rank
from app.models.uniform import Uniform


class InspectionLog(Base):
    __tablename__ = "inspection_log"

    inspection_id = Column(Integer, primary_key=True, index=True)
    access_id = Column(Integer, ForeignKey(AccessLog.access_id), nullable=False)
    affiliation = Column(Integer, ForeignKey(Affiliation.affiliation_id), nullable=False)
    rank = Column(Integer, ForeignKey(Rank.rank_id), nullable=False)
    name = Column(String(5), nullable=False)
    uniform = Column(Integer, ForeignKey(Uniform.uniform_id), nullable=False)
    image_path = Column(String(128), unique=True, nullable=False)
    checked = Column(Boolean, default=False)
