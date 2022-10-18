from sqlalchemy import Column, Integer, ForeignKey, UniqueConstraint
from app.db.base_schema import Base
from app.models.military_unit import MilitaryUnit
from app.models.guardhouse import Guardhouse


class UnitHouseRelation(Base):
    __tablename__ = "unit_house_relation"

    relation_id = Column(Integer, primary_key=True, index=True)
    military_unit = Column(Integer, ForeignKey(MilitaryUnit.unit_id), nullable=False)
    guardhouse = Column(Integer, ForeignKey(Guardhouse.house_id), nullable=False)
    __table_args__ = (UniqueConstraint("military_unit", "guardhouse", name="_unit_guardhouse_uc"),)
