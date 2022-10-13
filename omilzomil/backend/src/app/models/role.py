from sqlalchemy import Column, Integer, String
from app.db.base_schema import Base


class Role(Base):
    __tablename__ = "role"

    id = Column(Integer, primary_key=True, index=True)
    role = Column(String(9), unique=True, nullable=False)
