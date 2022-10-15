from datetime import datetime
from sqlalchemy import or_
from sqlalchemy.orm import Session
from app.models.access_log import AccessLog
from app.models.inspection_log import InspectionLog
from app.models.inspection_detail import InspectionDetail


def get_monthly_overall_stats(db: Session, military_unit: int = None, date: datetime = None, category: str = None, status: bool = None):
    if date is None:
        date = datetime.now()

    log = (
        db.query(InspectionLog)
        .join(AccessLog, AccessLog.access_id == InspectionLog.access_id)
        .join(InspectionDetail, InspectionLog.inspection_id == InspectionDetail.inspection_id)
        .filter(AccessLog.access_time.like(date.strftime("%Y-%m-%%")))
    )

    if military_unit is not None:
        log = log.filter(or_(AccessLog.military_unit == military_unit, AccessLog.military_unit == 0))
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


def get_monthly_detailed_stats(db: Session, appearance_type: int, military_unit: int = None, date: datetime = None, status: bool = None):
    if date is None:
        date = datetime.now()

    log = (
        db.query(InspectionLog)
        .join(AccessLog, AccessLog.access_id == InspectionLog.access_id)
        .join(InspectionDetail, InspectionLog.inspection_id == InspectionDetail.inspection_id)
        .filter(AccessLog.access_time.like(date.strftime("%Y-%m-%%")))
        .filter(InspectionDetail.appearance_type == appearance_type)
    )

    if military_unit is not None:
        log = log.filter(or_(AccessLog.military_unit == military_unit, AccessLog.military_unit == 0))
    if status is not None:
        count = log.filter(InspectionDetail.status == status).count()
    else:
        count = log.count()

    return count
