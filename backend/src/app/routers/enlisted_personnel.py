from fastapi import APIRouter, Depends, Body
from sqlalchemy.orm import Session
from core.db import get_db
import app.schemas.enlisted_personnel as schema
import app.crud.enlisted_personnel as crud


router = APIRouter(
    prefix="/enlisted",
    tags=["장병 복장 정보"],
)


@router.get("/{personnel_id}")
async def get_enlisted_personnel_by_id(personnel_id: int, db: Session = Depends(get_db)):
    return crud.get_enlisted_personnel_by_id(db, personnel_id)


@router.put("/{personnel_id}")
async def update_enlisted_personnel(personnel_id: int, personnel: schema.EnlistedPersonnelUpdate = Body(), db: Session = Depends(get_db)):
    crud.update_enlisted_personnel(db, personnel_id, personnel)
    res = {"success": True, "message": "Personnel info successfully updated"}
    return res
