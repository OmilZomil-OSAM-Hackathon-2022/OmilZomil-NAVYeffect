import sqlalchemy.exc
from sqlalchemy.orm import Session
from app.models.military_unit import MilitaryUnit
from app.schemas.military_unit import MilitaryUnitResponse


def create_military_unit(db: Session, unit: str):
    try:
        unit = MilitaryUnit(unit=unit)
        db.add(unit)
        db.commit()
        db.refresh(unit)
        return MilitaryUnitResponse(success=True, message="success")
    except sqlalchemy.exc.IntegrityError:
        return MilitaryUnitResponse(success=False, message="duplicate entry")


def get_military_unit(db: Session):
    return db.query(MilitaryUnit).all()


def update_military_unit(db: Session, old_unit: str, new_unit: str):
    unit = db.query(MilitaryUnit).filter_by(unit=old_unit)
    if not unit.count():
        return MilitaryUnitResponse(success=False, message="entry not found")
    try:
        unit.update({"unit": new_unit})
        db.commit()
        return MilitaryUnitResponse(success=True, message="success")
    except sqlalchemy.exc.IntegrityError:
        return MilitaryUnitResponse(success=False, message="unique key constraint fail")


def delete_military_unit(db: Session, unit: str):
    unit = db.query(MilitaryUnit).filter_by(unit=unit)
    if not unit.count():
        return MilitaryUnitResponse(success=False, message="entry not found")
    else:
        unit.delete()
        db.commit()
        return MilitaryUnitResponse(success=True, message="success")
