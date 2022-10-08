from sqlalchemy import Column, Integer, String
from app.db.base_schema import Base


class Uniform(Base):
    __tablename__ = "uniform"

    id = Column(Integer, primary_key=True, index=True)
    uniform = Column(String(3), unique=True, nullable=False)
