import sqlalchemy.exc
from sqlalchemy.orm import Session
from app.models.military_unit import MilitaryUnit


def create_military_unit(db: Session, unit: str):
    try:
        unit = MilitaryUnit(unit=unit)
        db.add(unit)
        db.commit()
        db.refresh(unit)
        return unit
    except sqlalchemy.exc.IntegrityError:
        return None


def get_military_unit(db: Session):
    return db.query(MilitaryUnit).all()


def update_military_unit(db: Session, old_unit: str, new_unit: str):
    res = db.query(MilitaryUnit).filter_by(unit=old_unit).update({"unit": new_unit})
    db.commit()
    return res


def delete_military_unit(db: Session, unit: str):
    res = db.query(MilitaryUnit).filter_by(unit=unit).delete()
    db.commit()
    return res
