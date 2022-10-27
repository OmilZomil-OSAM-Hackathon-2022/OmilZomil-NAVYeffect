from datetime import datetime
import sqlalchemy.exc
from sqlalchemy.orm import Session
from app.models.unit_house_relation import Guardhouse, UnitHouseRelation
from app.schemas.unit_house_relation import UnitHouseRelationResponse
from app.crud.military_unit import get_military_unit
from app.crud.guardhouse import get_guardhouse
from app.crud.vacation import get_unit_names_from_user


def create_unit_house_relation(db: Session, unit_id: int, house_id: int):
    if unit_id == 1 or not get_military_unit(db, unit_id).success:
        return UnitHouseRelationResponse(success=False, message="no entry found for military unit")
    if not get_guardhouse(db, house_id).success:
        return UnitHouseRelationResponse(success=False, message="no entry found for guardhouse")

    try:
        unit = UnitHouseRelation(military_unit=unit_id, guardhouse=house_id)
        db.add(unit)
        db.commit()
        db.refresh(unit)
        return UnitHouseRelationResponse(success=True, message=house_id)
    except sqlalchemy.exc.IntegrityError:
        return UnitHouseRelationResponse(success=False, message="unique key constraint fail")


def get_unit_house_relations(db: Session, unit_id: int, house: str = None):
    house = house and f"%{house}%" or "%"
    return (
        db.query(Guardhouse)
        .join(UnitHouseRelation, Guardhouse.house_id == UnitHouseRelation.guardhouse)
        .filter(UnitHouseRelation.military_unit == unit_id)
        .filter(Guardhouse.house.like(house))
        .order_by(Guardhouse.house)
        .all()
    )


def get_unit_from_house(db: Session, house: int, access_time: datetime, affiliation: int = None, rank: int = None, name: str = None):
    query = db.query(UnitHouseRelation.military_unit).filter_by(guardhouse=house)
    count = query.count()
    if count == 0:
        return 1
    elif count == 1:
        return query.first().military_unit
    else:
        units = get_unit_names_from_user(db, access_time, affiliation, rank, name)
        if len(units) == 1:
            return units[0].unit_id
        else:
            return 1


def delete_unit_house_relation(db: Session, unit_id: int, house_id: int):
    relation = db.query(UnitHouseRelation).filter_by(military_unit=unit_id).filter_by(guardhouse=house_id)
    if not relation.count():
        return UnitHouseRelationResponse(success=False, message="entry not found")
    else:
        relation.delete()
        db.commit()
        return UnitHouseRelationResponse(success=True, message=house_id)
