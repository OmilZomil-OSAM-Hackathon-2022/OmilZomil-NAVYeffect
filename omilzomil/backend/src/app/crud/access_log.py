from sqlalchemy.orm import Session
from app.models.access_log import AccessLog
from app.schemas.access_log import AccessLogCreate


def get_access_log_by_id(db: Session, access_id: int):
    return db.query(AccessLog).get(access_id)


def create_access_log(db: Session, access: AccessLogCreate):
    access_log = AccessLog(military_base=access.military_base, access_time=access.access_time, image_path=access.image)
    db.add(access_log)
    db.commit()
    db.refresh(access_log)
    return access_log
