from fastapi import APIRouter, Depends, Body
from sqlalchemy.orm import Session
from app import crud, schemas
from app.api import deps


router = APIRouter()


@router.get("/{personnel_id}", response_model=schemas.enlisted_personnel.EnlistedPersonnelRead)
async def get_personnel_info_by_id(personnel_id: int, db: Session = Depends(deps.get_db)):
    personnel_info = crud.enlisted_personnel.get_personnel_info_by_id(db, personnel_id)
    if personnel_info is None:
        personnel_info = schemas.enlisted_personnel.EnlistedPersonnelRead(success=False, message="Personnel info not found")
    return personnel_info


@router.put("/{personnel_id}", response_model=schemas.enlisted_personnel.EnlistedPersonnelUpdateResult)
async def update_personnel_info(personnel_id: int, personnel: schemas.enlisted_personnel.EnlistedPersonnelUpdate = Body(), db: Session = Depends(deps.get_db)):
    if crud.enlisted_personnel.get_personnel_info_by_id(db, personnel_id) is not None:
        crud.enlisted_personnel.update_personnel_info(db, personnel_id, personnel)
        res = schemas.enlisted_personnel.EnlistedPersonnelUpdateResult(success=True, message="Personnel info successfully updated")
    else:
        res = schemas.enlisted_personnel.EnlistedPersonnelUpdateResult(success=False, message="Personnel info not found")
    return res
