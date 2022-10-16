from sqlalchemy import Column, Integer, String
from app.db.base_schema import Base


class Rank(Base):
    __tablename__ = "rank"

    rank_id = Column(Integer, primary_key=True, index=True)
    rank = Column(String(8), unique=True, nullable=False)
