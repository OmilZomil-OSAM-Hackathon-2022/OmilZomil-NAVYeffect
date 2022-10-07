from sqlalchemy.orm import Session
from app.models.inspection_log import InspectionLog
from app.schemas.inspection_log import InspectionLogCreate, InspectionLogUpdate


def get_inspection_log_by_id(db: Session, inspection_id: int):
    return db.query(InspectionLog).get(inspection_id)


def create_inspection_log(db: Session, inspection: InspectionLogCreate):
    inspection = InspectionLog(
        access_id=inspection.access_id,
        affiliation=inspection.affiliation,
        name=inspection.name,
        rank=inspection.rank,
        uniform=inspection.uniform,
        has_name=inspection.has_name,
        has_rank=inspection.has_rank,
        has_neckerchief=inspection.has_neckerchief,
        has_muffler=inspection.has_muffler,
        has_flag=inspection.has_flag,
    )
    db.add(inspection)
    db.commit()
    db.refresh(inspection)
    return inspection


def update_inspection_log(db: Session, inspection_id: int, inspection: InspectionLogUpdate):
    inspection = {x: y for x, y in inspection.dict().items() if y is not None}
    db.query(InspectionLog).filter_by(inspection_id=inspection_id).update(inspection)
    db.commit()
