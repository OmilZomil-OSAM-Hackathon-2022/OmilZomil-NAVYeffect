from datetime import datetime
from sqlalchemy import or_
from sqlalchemy.orm import Session
from app.models.access_log import AccessLog
from app.models.inspection_log import InspectionLog
from app.models.inspection_detail import InspectionDetail


def get_monthly_unit_stats(db: Session, unit: int, date: datetime = None, category: str = None, status: bool = None):
    if date is None:
        date = datetime.now()

    log = (
        db.query(InspectionLog)
        .join(AccessLog, AccessLog.access_id == InspectionLog.access_id)
        .join(InspectionDetail, InspectionLog.inspection_id == InspectionDetail.inspection_id)
        .filter(or_(AccessLog.military_unit == unit, AccessLog.military_unit == 0))
        .filter(AccessLog.access_time.like(date.strftime("%Y-%m-%%")))
    )

    if category == "hair":
        log = log.filter(InspectionDetail.appearance_type == 1)
    elif category == "appearance":
        log = log.filter(InspectionDetail.appearance_type > 1)

    total = log.group_by(InspectionLog.inspection_id).count()
    if status is not None:
        count = log.filter(InspectionDetail.status == False).group_by(InspectionLog.inspection_id).count()
        if status:
            count = total - count
    else:
        count = total

    return count
