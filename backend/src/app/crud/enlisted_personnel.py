from sqlalchemy.orm import Session
from app.models.enlisted_personnel import EnlistedPersonnel
from app.schemas.enlisted_personnel import EnlistedPersonnelCreate, EnlistedPersonnelUpdate


def get_enlisted_personnel_by_id(db: Session, personnel_id: int):
    return db.query(EnlistedPersonnel).get(personnel_id)


def create_enlisted_personnel(db: Session, personnel: EnlistedPersonnelCreate):
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


def update_enlisted_personnel(db: Session, personnel_id: int, personnel: EnlistedPersonnelUpdate):
    personnel = {x: y for x, y in personnel.dict().items() if y is not None}
    db.query(EnlistedPersonnel).filter_by(personnel_id=personnel_id).update(personnel)
    db.commit()
