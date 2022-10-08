from sqlalchemy.orm import Session
from app.models.inspection_log import InspectionLog
from app.schemas.inspection_log import InspectionLogCreate, InspectionLogUpdate


def get_inspection_log_by_id(db: Session, log_id: int):
    return db.query(InspectionLog).get(log_id)


def create_inspection_log(db: Session, log: InspectionLogCreate):
    log = InspectionLog(
        access_id=log.access_id,
        affiliation=log.affiliation,
        name=log.name,
        rank=log.rank,
        uniform=log.uniform,
        has_name=log.has_name,
        has_rank=log.has_rank,
        has_neckerchief=log.has_neckerchief,
        has_muffler=log.has_muffler,
        has_flag=log.has_flag,
    )
    db.add(log)
    db.commit()
    db.refresh(log)
    return log


def update_inspection_log(db: Session, log_id: int, log: InspectionLogUpdate):
    log = {x: y for x, y in log.dict().items() if y is not None}
    db.query(InspectionLog).filter_by(inspection_id=log_id).update(log)
    db.commit()
