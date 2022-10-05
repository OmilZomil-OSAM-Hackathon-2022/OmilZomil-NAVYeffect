from fastapi import APIRouter, Depends, Body
from sqlalchemy.orm import Session
from core.db import get_db
from app.enlisted_personnel.schema import EnlistedPersonnelUpdate
from app.enlisted_personnel import crud


router = APIRouter(
    prefix="/enlisted",
    tags=["장병 정보"],
)


@router.get("/{personnel_id}")
async def get_enlisted_personnel_by_id(personnel_id: int, db: Session = Depends(get_db)):
    return crud.get_personnel_by_id(db, personnel_id)


@router.put("/{personnel_id}")
async def update_enlisted_personnel(personnel_id: int, personnel: EnlistedPersonnelUpdate = Body(), db: Session = Depends(get_db)):
    crud.update_personnel(db, personnel_id, personnel)
    res = {"success": True, "message": "Personnel info successfully updated"}
    return res
