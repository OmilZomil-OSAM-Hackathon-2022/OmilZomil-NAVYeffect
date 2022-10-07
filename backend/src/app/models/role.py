from sqlalchemy import Column, Integer, String
from app.db.base_schema import Base


class Role(Base):
    __tablename__ = "role"

    role_id = Column(Integer, primary_key=True, index=True)
    role = Column(String(6), unique=True, nullable=False)
