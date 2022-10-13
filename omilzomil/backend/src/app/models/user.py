from sqlalchemy import Column, Integer, String, ForeignKey
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
    affiliation = Column(String(6), ForeignKey(Affiliation.affiliation), nullable=False)
    military_unit = Column(String(128), ForeignKey(MilitaryUnit.unit), nullable=False)
    rank = Column(String(4), ForeignKey(Rank.rank), nullable=False)
    username = Column(String(33), unique=True, nullable=False)
    password = Column(String(129), nullable=False)
    role = Column(Integer, ForeignKey(Role.role_id), default=4)
