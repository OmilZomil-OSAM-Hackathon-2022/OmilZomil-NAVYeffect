from typing import Optional
from fastapi import APIRouter, Depends, Body
from fastapi_pagination import paginate, Page, Params
from sqlalchemy.orm import Session
from app.crud import military_unit as crud
from app.schemas import military_unit as schema
from app.api import deps
from app.schemas.user import UserReadResponse


router = APIRouter()


@router.post("/", response_model=schema.MilitaryUnitResponse)
async def create_military_unit(
    unit: schema.MilitaryUnitCreate = Body(), db: Session = Depends(deps.get_db), current_user: UserReadResponse = Depends(deps.get_current_active_super)
):
    if not current_user.success:
        return schema.MilitaryUnitResponse(success=False, message=current_user.message)

    return crud.create_military_unit(db, unit.unit)


@router.get("/", response_model=Page[schema.MilitaryUnitRead])
async def get_military_units(unit: Optional[str] = None, db: Session = Depends(deps.get_db), params: Params = Depends()):
    return paginate(crud.get_military_units(db, unit=unit), params)


@router.get("/{unit_id}", response_model=schema.MilitaryUnitReadResponse)
def get_military_unit(unit_id: int, db: Session = Depends(deps.get_db)):
    return crud.get_military_unit(db, unit_id)


@router.put("/{unit_id}", response_model=schema.MilitaryUnitResponse)
async def update_military_unit(
    unit_id: int,
    new_unit: schema.MilitaryUnitUpdate = Body(),
    db: Session = Depends(deps.get_db),
    current_user: UserReadResponse = Depends(deps.get_current_active_super),
):
    if not current_user.success:
        return schema.MilitaryUnitResponse(success=False, message=current_user.message)

    return crud.update_military_unit(db, unit_id, new_unit.unit)


@router.delete("/{unit_id}", response_model=schema.MilitaryUnitResponse)
def delete_military_unit(unit_id: int, db: Session = Depends(deps.get_db), current_user: UserReadResponse = Depends(deps.get_current_active_super)):
    if not current_user.success:
        return schema.MilitaryUnitResponse(success=False, message=current_user.message)

    return crud.delete_military_unit(db, unit_id)
