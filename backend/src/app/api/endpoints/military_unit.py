from typing import List
from fastapi import APIRouter, Depends, Body
from sqlalchemy.orm import Session
from app.crud import military_unit as crud
from app.schemas import military_unit as schema
from app.api import deps


router = APIRouter()


@router.post("/", response_model=schema.MilitaryUnitResponse)
async def create_military_unit(unit: schema.MilitaryUnitCreate = Body(), db: Session = Depends(deps.get_db)):
    if crud.create_military_unit(db, unit.unit) is not None:
        res = schema.MilitaryUnitResponse(success=True, message="success")
    else:
        res = schema.MilitaryUnitResponse(success=False, message="duplicate entry")
    return res


@router.get("/", response_model=List[schema.MilitaryUnitRead])
def get_military_unit(db: Session = Depends(deps.get_db)):
    return [schema.MilitaryUnitRead(unit=unit.unit) for unit in crud.get_military_unit(db)]


@router.put("/{unit}", response_model=schema.MilitaryUnitResponse)
async def update_military_unit(unit: str, new_unit: schema.MilitaryUnitUpdate = Body(), db: Session = Depends(deps.get_db)):
    res = crud.update_military_unit(db, unit, new_unit.unit)
    if res:
        res = schema.MilitaryUnitResponse(success=True, message="success")
    elif res is not None:
        res = schema.MilitaryUnitResponse(success=False, message="entry not found")
    else:
        res = schema.MilitaryUnitResponse(success=False, message="duplicate entry")
    return res


@router.delete("/{unit}", response_model=schema.MilitaryUnitResponse)
def delete_military_unit(unit: str, db: Session = Depends(deps.get_db)):
    if crud.delete_military_unit(db, unit):
        res = schema.MilitaryUnitResponse(success=True, message="success")
    else:
        res = schema.MilitaryUnitResponse(success=False, message="entry not found")
    return res
