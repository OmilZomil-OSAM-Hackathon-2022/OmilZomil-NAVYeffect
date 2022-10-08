from typing import List
from fastapi import APIRouter, Depends, Body
from sqlalchemy.orm import Session
from app.crud import military_unit as crud
from app.schemas import military_unit as schema
from app.api import deps


router = APIRouter()


@router.post("/", response_model=schema.MilitaryUnitResponse)
async def create_military_unit(unit: schema.MilitaryUnitCreate = Body(), db: Session = Depends(deps.get_db)):
    return crud.create_military_unit(db, unit.unit)


@router.get("/", response_model=List[schema.MilitaryUnitRead])
def get_military_unit(db: Session = Depends(deps.get_db)):
    return [schema.MilitaryUnitRead(unit=unit.unit) for unit in crud.get_military_unit(db)]


@router.put("/{unit}", response_model=schema.MilitaryUnitResponse)
async def update_military_unit(unit: str, new_unit: schema.MilitaryUnitUpdate = Body(), db: Session = Depends(deps.get_db)):
    return crud.update_military_unit(db, unit, new_unit.unit)


@router.delete("/{unit}", response_model=schema.MilitaryUnitResponse)
def delete_military_unit(unit: str, db: Session = Depends(deps.get_db)):
    return crud.delete_military_unit(db, unit)
