from sqlalchemy.orm import Session
from app.base_access.model import BaseAccess
from app.base_access.schema import BaseAccessCreate


def get_access_by_id(db: Session, access_id: int):
    return db.query(BaseAccess).filter(BaseAccess.access_id == access_id).first()


def create_access(db: Session, bac: BaseAccessCreate):
    base_access = BaseAccess(base_name=bac.base_name, access_time=bac.access_time, image=bac.image)
    db.add(base_access)
    db.commit()
    db.refresh(base_access)
    return base_access
