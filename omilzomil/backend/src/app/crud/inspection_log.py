import sqlalchemy.exc
from sqlalchemy.orm import Session
from app.models.inspection_log import InspectionLog
from app.schemas.inspection_log import InspectionLogCreate, InspectionLogUpdateInformation, InspectionLogUpdateCheck, InspectionLogResponse


def create_inspection_log(db: Session, log: InspectionLogCreate):
    try:
        log = InspectionLog(
            access_id=log.access_id,
            affiliation=log.affiliation,
            rank=log.rank,
            name=log.name,
            uniform=log.uniform,
            image_path=log.image_path,
        )
        db.add(log)
        db.commit()
        db.refresh(log)
        return InspectionLogResponse(success=True, message=log.inspection_id)
    except sqlalchemy.exc.IntegrityError as e:
        if "foreign key constraint fail" in e.orig.args[1]:
            return InspectionLogResponse(success=False, message="foreign key constraint fail")
        elif "Duplicate entry" in e.orig.args[1]:
            return InspectionLogResponse(success=False, message="unique key constraint fail")
        raise e


def update_inspection_log_information(db: Session, log_id: int, information: InspectionLogUpdateInformation):
    log = db.query(InspectionLog).filter_by(inspection_id=log_id)
    if not log.count():
        return InspectionLogResponse(success=False, message="entry not found")
    try:
        information = {x: y for x, y in information.dict().items() if y is not None}
        log.update(information)
        db.commit()
        return InspectionLogResponse(success=True, message=log_id)
    except sqlalchemy.exc.IntegrityError as e:
        if "foreign key constraint fail" in e.orig.args[1]:
            return InspectionLogResponse(success=False, message="foreign key constraint fail")
        elif "Duplicate entry" in e.orig.args[1]:
            return InspectionLogResponse(success=False, message="unique key constraint fail")
        raise e


def update_inspection_log_check(db: Session, log_id: int, checked: InspectionLogUpdateCheck):
    log = db.query(InspectionLog).filter_by(inspection_id=log_id)
    if not log.count():
        return InspectionLogResponse(success=False, message="entry not found")

    log.update(checked.dict())
    db.commit()
    return InspectionLogResponse(success=True, message=log_id)
