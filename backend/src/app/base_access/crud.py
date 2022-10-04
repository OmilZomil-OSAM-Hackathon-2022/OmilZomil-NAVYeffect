from sqlalchemy.orm import Session
from app.base_access.model import BaseAccess
from app.base_access.schema import BaseAccessCreate


def get_access_by_id(db: Session, access_id: int):
    return db.query(BaseAccess).filter(BaseAccess.access_id == access_id).first()


def create_access(db: Session, access: BaseAccessCreate):
    base_access = BaseAccess(base_name=access.base_name, access_time=access.access_time, image=access.image)
    db.add(base_access)
    db.commit()
    db.refresh(base_access)
    return base_access
