from sqlalchemy import Column, Integer, Date, Boolean, ForeignKey
from app.db.base_schema import Base
from app.models.user import User


class Vacation(Base):
    __tablename__ = "vacation"

    vacation_id = Column(Integer, primary_key=True, index=True)
    user = Column(Integer, ForeignKey(User.user_id), nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    confirmed = Column(Boolean, default=False)
