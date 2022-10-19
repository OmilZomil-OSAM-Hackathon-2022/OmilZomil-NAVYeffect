from datetime import date, datetime
from sqlalchemy import or_
from sqlalchemy.orm import Session
from app.models.inspection_log import InspectionLog
from app.models.inspection_detail import InspectionDetail


def get_logs(db: Session, military_unit: int, rank: int = None, name: str = None, appearance_type: int = None, start_date: date = None, end_date: date = None):
    subquery = (
        db.query(InspectionLog.inspection_id)
        .join(InspectionDetail, InspectionLog.inspection_id == InspectionDetail.inspection_id)
        .filter(or_(InspectionLog.military_unit == 1, InspectionLog.military_unit == military_unit))
    )

    if rank is not None:
        subquery = subquery.filter(InspectionLog.rank == rank)
    if name is not None:
        subquery = subquery.filter(InspectionLog.name.like(f"%{name}%"))
    if appearance_type is not None:
        subquery = subquery.filter(InspectionDetail.appearance_type == appearance_type).filter(InspectionDetail.status == False)
    if start_date is not None and end_date is not None:
        start_date = datetime(*start_date.timetuple()[:6])
        end_date = datetime(*end_date.timetuple()[:6])
        subquery = subquery.filter(InspectionLog.access_time >= start_date).filter(InspectionLog.access_time <= end_date)

    query = (
        db.query(InspectionLog)
        .join(InspectionDetail, InspectionLog.inspection_id == InspectionDetail.inspection_id)
        .filter(InspectionLog.inspection_id.in_(subquery))
    )

    hair_status = query.filter(InspectionDetail.appearance_type == 1).filter(InspectionDetail.status == False).count() == 0
    appearance_status = query.filter(InspectionDetail.appearance_type > 1).filter(InspectionDetail.status == False).count() == 0

    ret = list()
    for entry in query.all():
        ret.append(
            {
                "inspection_id": entry.inspection_id,
                "access_time": entry.access_time,
                "affiliation": entry.affiliation,
                "rank": entry.rank,
                "name": entry.name,
                "uniform": entry.uniform,
                "hair_status": hair_status,
                "appearance_status": appearance_status,
                "image_path": entry.image_path,
                "is_checked": entry.is_checked,
            }
        )

    return ret
