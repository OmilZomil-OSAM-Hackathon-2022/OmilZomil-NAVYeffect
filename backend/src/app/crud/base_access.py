from sqlalchemy.orm import Session
from app.models.base_access import BaseAccess
from app.schemas.base_access import BaseAccessCreate


def get_access_log_by_id(db: Session, access_id: int):
    return db.query(BaseAccess).get(access_id)


def create_access_log(db: Session, access: BaseAccessCreate):
    base_access = BaseAccess(base_name=access.base_name, access_time=access.access_time, image=access.image)
    db.add(base_access)
    db.commit()
    db.refresh(base_access)
    return base_access
