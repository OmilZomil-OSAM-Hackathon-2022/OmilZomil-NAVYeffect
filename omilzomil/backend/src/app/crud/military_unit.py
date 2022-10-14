import sqlalchemy.exc
from sqlalchemy.orm import Session
from app.models.military_unit import MilitaryUnit
from app.schemas.military_unit import MilitaryUnitResponse, MilitaryUnitReadResponse


def create_military_unit(db: Session, unit: str):
    try:
        unit = MilitaryUnit(unit=unit)
        db.add(unit)
        db.commit()
        db.refresh(unit)
        return MilitaryUnitResponse(success=True, message="success")
    except sqlalchemy.exc.IntegrityError:
        return MilitaryUnitResponse(success=False, message="unique key constraint fail")


def get_military_units(db: Session):
    return db.query(MilitaryUnit).all()


def get_military_unit(db: Session, unit: str):
    unit = db.query(MilitaryUnit).filter(MilitaryUnit.unit.like(f"%{unit}%"))
    if not unit.count():
        return MilitaryUnitReadResponse(success=False, message="entry not found")

    unit = unit.first()
    unit = MilitaryUnitReadResponse(
        success=True,
        message="success",
        unit_id=unit.unit_id,
        unit=unit.unit,
    )
    return unit


def update_military_unit(db: Session, unit_id: int, new_unit: str):
    old_unit = db.query(MilitaryUnit).filter_by(unit_id=unit_id)
    if not old_unit.count():
        return MilitaryUnitResponse(success=False, message="entry not found")
    try:
        old_unit.update({"unit": new_unit})
        db.commit()
        return MilitaryUnitResponse(success=True, message="success")
    except sqlalchemy.exc.IntegrityError:
        return MilitaryUnitResponse(success=False, message="unique key constraint fail")


def delete_military_unit(db: Session, unit_id: int):
    unit = db.query(MilitaryUnit).filter_by(unit_id=unit_id)
    if not unit.count():
        return MilitaryUnitResponse(success=False, message="entry not found")
    else:
        unit.delete()
        db.commit()
        return MilitaryUnitResponse(success=True, message="success")
