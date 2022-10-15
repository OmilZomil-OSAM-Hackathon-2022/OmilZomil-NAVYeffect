from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from app.db.base_schema import Base
from app.models.affiliation import Affiliation
from app.models.military_unit import MilitaryUnit
from app.models.rank import Rank
from app.models.role import Role


class User(Base):
    __tablename__ = "user"

    user_id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(8), nullable=False)
    dog_number = Column(String(16), unique=True, nullable=False)
    affiliation = Column(Integer, ForeignKey(Affiliation.affiliation_id), nullable=False)
    military_unit = Column(Integer, ForeignKey(MilitaryUnit.unit_id), nullable=False)
    rank = Column(Integer, ForeignKey(Rank.rank_id), nullable=False)
    username = Column(String(33), unique=True, nullable=False)
    password = Column(String(129), nullable=False)
    role = Column(Integer, ForeignKey(Role.role_id), default=1)
    is_active = Column(Boolean, default=False)
