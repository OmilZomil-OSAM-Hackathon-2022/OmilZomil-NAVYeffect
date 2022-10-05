from sqlalchemy.orm import Session
from app.enlisted_personnel.model import EnlistedPersonnel
from app.enlisted_personnel.schema import EnlistedPersonnelCreate


def get_personnel_by_id(db: Session, personnel_id: int):
    return db.query(EnlistedPersonnel).get(personnel_id)


def create_personnel(db: Session, personnel: EnlistedPersonnelCreate):
    personnel = EnlistedPersonnel(
        access_id=personnel.access_id,
        army_type=personnel.army_type,
        name=personnel.name,
        rank=personnel.rank,
        uniform_type=personnel.uniform_type,
        has_name=personnel.has_name,
        has_rank=personnel.has_rank,
        has_neckerchief=personnel.has_neckerchief,
        has_muffler=personnel.has_muffler,
        has_flag=personnel.has_flag,
    )
    db.add(personnel)
    db.commit()
    db.refresh(personnel)
    return personnel
