from typing import List
from fastapi import APIRouter, Depends, Body
from sqlalchemy.orm import Session
from app.crud import military_unit as crud
from app.schemas import military_unit as schema
from app.api import deps


router = APIRouter()


@router.post("/", response_model=schema.MilitaryUnitCreate)
async def create_military_unit(unit: schema.MilitaryUnitCreate = Body(), db: Session = Depends(deps.get_db)):
    res = schema.MilitaryUnitCreate(success=True, message="create successful", unit=unit.unit)
    if crud.create_military_unit(db, unit.unit) is None:
        res.success = False
        res.message = "duplicate entry"
    return res


@router.get("/", response_model=List[schema.MilitaryUnitRead])
def get_military_unit(db: Session = Depends(deps.get_db)):
    return [schema.MilitaryUnitRead(success=True, message="read successful", unit=unit.unit) for unit in crud.get_military_unit(db)]


@router.put("/{old_unit}", response_model=schema.MilitaryUnitUpdate)
async def update_military_unit(old_unit: str, new_unit: schema.MilitaryUnitUpdate = Body(), db: Session = Depends(deps.get_db)):
    res = schema.MilitaryUnitUpdate(success=True, message="update successful", unit=new_unit.unit)
    if not crud.update_military_unit(db, old_unit, new_unit.unit):
        res.success = False
        res.message = "entry not found"
    return res


@router.delete("/{unit}", response_model=schema.MilitaryUnitDelete)
def delete_military_unit(unit: str, db: Session = Depends(deps.get_db)):
    res = schema.MilitaryUnitDelete(success=True, message="delete successful", unit=unit)
    if not crud.delete_military_unit(db, unit):
        res.success = False
        res.message = "entry not found"
    return res
