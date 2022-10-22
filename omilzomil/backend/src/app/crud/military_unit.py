import sqlalchemy.exc
from sqlalchemy.orm import Session
from app.models.military_unit import MilitaryUnit
from app.schemas.military_unit import MilitaryUnitResponse, MilitaryUnitReadResponse


def create_military_unit(db: Session, unit: str, unit_id: int = None):
    try:
        if unit_id is None:
            unit = MilitaryUnit(unit=unit)
        else:
            unit = MilitaryUnit(unit_id=unit_id, unit=unit)
        db.add(unit)
        db.commit()
        db.refresh(unit)
        return MilitaryUnitResponse(success=True, message=unit.unit_id)
    except sqlalchemy.exc.IntegrityError:
        return MilitaryUnitResponse(success=False, message="unique key constraint fail")


def get_military_units(db: Session, unit: str = None, page: int = 1):
    unit = unit and f"%{unit}%" or "%"
    return (
        db.query(MilitaryUnit)
        .filter(MilitaryUnit.unit_id != 1)
        .filter(MilitaryUnit.unit.like(unit))
        .order_by(MilitaryUnit.unit)
        .offset((page - 1) * 10)
        .limit(10)
        .all()
    )


def get_military_unit(db: Session, unit_id: int):
    unit = db.query(MilitaryUnit).get(unit_id)
    if unit is None:
        return MilitaryUnitReadResponse(success=False, message="entry not found")
    else:
        return MilitaryUnitReadResponse(success=True, message="success", unit_id=unit.unit_id, unit=unit.unit)


def update_military_unit(db: Session, unit_id: int, new_unit: str):
    old_unit = db.query(MilitaryUnit).filter_by(unit_id=unit_id)
    if not old_unit.count():
        return MilitaryUnitResponse(success=False, message="entry not found")
    try:
        old_unit.update({"unit": new_unit})
        db.commit()
        return MilitaryUnitResponse(success=True, message=unit_id)
    except sqlalchemy.exc.IntegrityError:
        return MilitaryUnitResponse(success=False, message="unique key constraint fail")


def delete_military_unit(db: Session, unit_id: int):
    unit = db.query(MilitaryUnit).filter_by(unit_id=unit_id)
    if not unit.count():
        return MilitaryUnitResponse(success=False, message="entry not found")
    else:
        unit.delete()
        db.commit()
        return MilitaryUnitResponse(success=True, message=unit_id)
