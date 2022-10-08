from fastapi import APIRouter, Depends, Body
from sqlalchemy.orm import Session
from app.crud import enlisted_personnel as crud
from app.schemas import enlisted_personnel as schema
from app.api import deps


router = APIRouter()


@router.put("/{personnel_id}", response_model=schema.EnlistedPersonnelUpdateResult)
async def update_personnel_info(personnel_id: int, personnel: schema.EnlistedPersonnelUpdate = Body(), db: Session = Depends(deps.get_db)):
    if crud.get_personnel_info_by_id(db, personnel_id) is not None:
        res = schema.EnlistedPersonnelUpdateResult(success=True, message="Personnel info successfully updated")
    else:
        res = schema.EnlistedPersonnelUpdateResult(success=False, message="Personnel info not found")
    return res
