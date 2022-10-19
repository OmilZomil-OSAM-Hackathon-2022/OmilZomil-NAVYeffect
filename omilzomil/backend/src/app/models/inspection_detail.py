from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from app.db.base_schema import Base
from app.models.inspection_log import InspectionLog
from app.models.appearance import Appearance


class InspectionDetail(Base):
    __tablename__ = "inspection_detail"

    detail_id = Column(Integer, primary_key=True, index=True)
    inspection_id = Column(Integer, ForeignKey(InspectionLog.inspection_id), nullable=False)
    appearance_type = Column(Integer, ForeignKey(Appearance.appearance_id), nullable=False)
    status = Column(Boolean, nullable=False)
    is_valid = Column(Boolean, default=True)
    image_path = Column(String(128), nullable=False)
