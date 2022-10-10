from sqlalchemy import Column, Integer, String
from app.db.base_schema import Base


class Rank(Base):
    __tablename__ = "rank"

    id = Column(Integer, primary_key=True, index=True)
    rank = Column(String(4), unique=True, nullable=False)
