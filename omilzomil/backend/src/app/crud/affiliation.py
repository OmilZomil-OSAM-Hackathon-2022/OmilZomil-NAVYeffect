from sqlalchemy.orm import Session
from app.models.affiliation import Affiliation


def create_affiliation(db: Session, affiliation: str):
    affiliation = Affiliation(affiliation=affiliation)
    db.add(affiliation)
    db.commit()
    db.refresh(affiliation)
    return affiliation
