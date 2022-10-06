from fastapi import APIRouter, Depends, Body
from sqlalchemy.orm import Session
from app.crud import enlisted_personnel as crud
from app.schemas import enlisted_personnel as schema
from app.api import deps


router = APIRouter()


@router.get("/{personnel_id}", response_model=schema.EnlistedPersonnelRead)
async def get_personnel_info_by_id(personnel_id: int, db: Session = Depends(deps.get_db)):
    personnel_info = crud.get_personnel_info_by_id(db, personnel_id)
    if personnel_info is None:
        personnel_info = schema.EnlistedPersonnelRead(success=False, message="Personnel info not found")
    return personnel_info


@router.put("/{personnel_id}", response_model=schema.EnlistedPersonnelUpdateResult)
async def update_personnel_info(personnel_id: int, personnel: schema.EnlistedPersonnelUpdate = Body(), db: Session = Depends(deps.get_db)):
    if crud.get_personnel_info_by_id(db, personnel_id) is not None:
        crud.update_personnel_info(db, personnel_id, personnel)
        res = schema.EnlistedPersonnelUpdateResult(success=True, message="Personnel info successfully updated")
    else:
        res = schema.EnlistedPersonnelUpdateResult(success=False, message="Personnel info not found")
    return res
