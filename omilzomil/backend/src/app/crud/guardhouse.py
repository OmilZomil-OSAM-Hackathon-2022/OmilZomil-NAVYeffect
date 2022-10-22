import sqlalchemy.exc
from sqlalchemy.orm import Session
from app.models.guardhouse import Guardhouse
from app.schemas.guardhouse import GuardhouseResponse, GuardhouseReadResponse


def create_guardhouse(db: Session, house: str):
    try:
        house = Guardhouse(house=house)
        db.add(house)
        db.commit()
        db.refresh(house)
        return GuardhouseResponse(success=True, message=house.house_id)
    except sqlalchemy.exc.IntegrityError:
        return GuardhouseResponse(success=False, message="unique key constraint fail")


def get_guardhouses(db: Session, house: str = None, page: int = None):
    house = house and f"%{house}%" or "%"
    query = db.query(Guardhouse).filter(Guardhouse.house.like(house))

    if page is not None:
        query = query.order_by(Guardhouse.house).offset((page - 1) * 10).limit(10)

    return query.all()


def get_guardhouse(db: Session, house_id: int):
    house = db.query(Guardhouse).get(house_id)
    if house is None:
        return GuardhouseReadResponse(success=False, message="entry not found")
    else:
        return GuardhouseReadResponse(success=True, message="success", house_id=house.house_id, house=house.house)


def update_guardhouse(db: Session, house_id: int, new_house: str):
    old_house = db.query(Guardhouse).filter_by(house_id=house_id)
    if not old_house.count():
        return GuardhouseResponse(success=False, message="entry not found")
    try:
        old_house.update({"house": new_house})
        db.commit()
        return GuardhouseResponse(success=True, message=house_id)
    except sqlalchemy.exc.IntegrityError:
        return GuardhouseResponse(success=False, message="unique key constraint fail")


def delete_guardhouse(db: Session, house_id: int):
    house = db.query(Guardhouse).filter_by(house_id=house_id)
    if not house.count():
        return GuardhouseResponse(success=False, message="entry not found")
    else:
        house.delete()
        db.commit()
        return GuardhouseResponse(success=True, message=house_id)
