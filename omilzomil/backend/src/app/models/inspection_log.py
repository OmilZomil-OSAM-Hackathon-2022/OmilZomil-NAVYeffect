from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from app.db.base_schema import Base
from app.models.affiliation import Affiliation
from app.models.guardhouse import Guardhouse
from app.models.military_unit import MilitaryUnit
from app.models.rank import Rank
from app.models.uniform import Uniform


class InspectionLog(Base):
    __tablename__ = "inspection_log"

    inspection_id = Column(Integer, primary_key=True, index=True)
    guardhouse = Column(Integer, ForeignKey(Guardhouse.house_id), nullable=False)
    access_time = Column(DateTime, default=datetime.now())
    affiliation = Column(Integer, ForeignKey(Affiliation.affiliation_id), nullable=False)
    military_unit = Column(Integer, ForeignKey(MilitaryUnit.unit_id), default=1)
    rank = Column(Integer, ForeignKey(Rank.rank_id), nullable=False)
    name = Column(String(5), nullable=False)
    uniform = Column(Integer, ForeignKey(Uniform.uniform_id), nullable=False)
    image_path = Column(String(128), unique=True, nullable=False)
    is_checked = Column(Boolean, default=False)
