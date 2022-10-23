from datetime import date, datetime
from sqlalchemy import or_
import sqlalchemy.exc
from sqlalchemy.orm import Session
from app.models.inspection_log import InspectionLog
from app.models.inspection_detail import InspectionDetail
from app.schemas.inspection_log import InspectionLogUpdateCheck, InspectionLogUpdateInformation, InspectionLogResponse
from app.schemas.inspection_detail import InspectionDetailUpdateStatus, InspectionDetailUpdateValidity, InspectionDetailResponse


def get_logs(
    db: Session,
    military_unit: int = None,
    rank: int = None,
    name: str = None,
    appearance_type: int = None,
    start_date: date = None,
    end_date: date = None,
):
    subquery = db.query(InspectionLog.inspection_id).join(InspectionDetail, InspectionLog.inspection_id == InspectionDetail.inspection_id)

    if military_unit is not None:
        subquery = subquery.filter(or_(InspectionLog.military_unit == 1, InspectionLog.military_unit == military_unit))
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

    entries = db.query(InspectionLog).filter(InspectionLog.inspection_id.in_(subquery)).order_by(InspectionLog.access_time.desc()).all()

    logs = list()
    for entry in entries:
        query = db.query(InspectionDetail).filter_by(inspection_id=entry.inspection_id).filter(InspectionDetail.status == False)
        hair_status = query.filter(InspectionDetail.appearance_type == 1).count() == 0
        appearance_status = query.filter(InspectionDetail.appearance_type > 1).count() == 0

        log = {
            "inspection_id": entry.inspection_id,
            "access_time": entry.access_time,
            "affiliation": entry.affiliation,
            "military_unit": entry.military_unit,
            "rank": entry.rank,
            "name": entry.name,
            "uniform": entry.uniform,
            "hair_status": hair_status,
            "appearance_status": appearance_status,
            "image_path": entry.image_path,
            "is_checked": entry.is_checked,
        }
        logs.append(log)

    return logs


def get_log_details(db: Session, inspection_id: int):
    log = db.query(InspectionLog).get(inspection_id)
    if log is None:
        return list()

    types = list()
    if log.uniform == 2:
        types = [1, 2, 3, 5]
    elif log.uniform == 3:
        types = [1, 2, 3, 5, 6, 7]
    elif log.uniform == 4:
        types = [1, 2, 3, 4, 5]

    query = db.query(InspectionDetail).filter_by(inspection_id=inspection_id)

    details = list()
    for appearance_type in types:
        detail = query.filter_by(appearance_type=appearance_type)
        if detail.count() == 0:
            continue

        detail = detail.first()
        detail = {
            "detail_id": detail.detail_id,
            "apperance_type": detail.appearance_type,
            "status": detail.status,
            "is_valid": detail.is_valid,
            "image_path": detail.image_path,
        }
        details.append(detail)

    return details


def update_log_check(db: Session, inspection_id: int, is_checked: InspectionLogUpdateCheck):
    log = db.query(InspectionLog).filter_by(inspection_id=inspection_id)
    if not log.count():
        return InspectionLogResponse(success=False, message="entry not found")
    elif type(is_checked.is_checked) != bool:
        return InspectionLogResponse(success=False, message="invalid type")
    else:
        log.update(is_checked.dict())
        db.commit()
        return InspectionLogResponse(success=True, message=inspection_id)


def update_log_information(db: Session, inspection_id: int, information: InspectionLogUpdateInformation):
    log = db.query(InspectionLog).filter_by(inspection_id=inspection_id)
    if not log.count():
        return InspectionLogResponse(success=False, message="entry not found")

    try:
        information = {x: y for x, y in information.dict().items() if y is not None}
        log.update(information)
        db.commit()
        return InspectionLogResponse(success=True, message=inspection_id)
    except sqlalchemy.exc.IntegrityError:
        return InspectionLogResponse(success=False, message="foreign key constraint fail")


def update_log_detail_status(db: Session, detail_id: int, status: InspectionDetailUpdateStatus):
    detail = db.query(InspectionDetail).filter_by(detail_id=detail_id)
    if not detail.count():
        return InspectionDetailResponse(success=False, message="entry not found")
    elif type(status.status) != bool:
        return InspectionDetailResponse(success=False, message="invalid type")
    else:
        detail.update(status.dict())
        db.commit()
        return InspectionDetailResponse(success=True, message=detail_id)


def update_log_detail_validity(db: Session, detail_id: int, is_valid: InspectionDetailUpdateValidity):
    detail = db.query(InspectionDetail).filter_by(detail_id=detail_id)
    if not detail.count():
        return InspectionDetailResponse(success=False, message="entry not found")
    elif type(is_valid.is_valid) != bool:
        return InspectionDetailResponse(success=False, message="invalid type")
    else:
        detail.update(is_valid.dict())
        db.commit()
        return InspectionDetailResponse(success=True, message=detail_id)
