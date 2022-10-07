from sqlalchemy import Column, Integer, String, ForeignKey
from app.db.base_schema import Base


class User(Base):
    __tablename__ = "user"

    user_id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(8), nullable=False)
    dog_number = Column(String(16), unique=True, nullable=False)
    affiliation = Column(String(6), ForeignKey("affiliation.affiliation"), nullable=False)
    military_unit = Column(String(128), ForeignKey("military_unit.unit"), nullable=False)
    rank = Column(String(4), ForeignKey("rank.rank"), nullable=False)
    username = Column(String(17), unique=True, nullable=False)
    password = Column(String(17), nullable=False)
    role = Column(String(6), ForeignKey("role.role"), default="unauthorized")
