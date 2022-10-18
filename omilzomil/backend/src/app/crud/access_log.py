from sqlalchemy.orm import Session
from app.models.access_log import AccessLog
from app.schemas.access_log import AccessLogCreate, AccessLogResponse


def create_access_log(db: Session, log: AccessLogCreate):
    log = AccessLog(
        guardhouse=log.guardhouse,
        access_time=log.access_time,
    )
    db.add(log)
    db.commit()
    db.refresh(log)
    return AccessLogResponse(success=True, message=log.access_id)
