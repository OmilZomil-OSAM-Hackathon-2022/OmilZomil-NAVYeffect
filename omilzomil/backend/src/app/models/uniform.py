from sqlalchemy import Column, Integer, String
from app.db.base_schema import Base


class Uniform(Base):
    __tablename__ = "uniform"

    uniform_id = Column(Integer, primary_key=True, index=True)
    uniform = Column(String(8), unique=True, nullable=False)
