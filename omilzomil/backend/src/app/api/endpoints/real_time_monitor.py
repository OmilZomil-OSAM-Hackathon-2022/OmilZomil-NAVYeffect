from datetime import date
from typing import Optional
from fastapi import APIRouter, Depends, Body
from sqlalchemy.orm import Session
from app.schemas.user import UserReadResponse
from app.schemas.inspection_detail import InspectionDetailUpdateValidity
from app.crud import real_time_monitor as crud
from app.api import deps


router = APIRouter()


@router.get("/")
def get_logs(
    rank: Optional[int] = None,
    name: Optional[str] = None,
    appearance_type: Optional[int] = None,
    start_date: Optional[date] = None,
    end_date: Optional[date] = None,
    db: Session = Depends(deps.get_db),
    current_user: UserReadResponse = Depends(deps.get_current_user),
):
    if not current_user.success:
        return {"success": False, "message": current_user.message}

    return crud.get_logs(db, current_user.military_unit, rank, name, appearance_type, start_date, end_date)


@router.get("/detail/{inspection_id}")
def get_log_details(
    inspection_id,
    int,
    db: Session = Depends(deps.get_db),
    current_user: UserReadResponse = Depends(deps.get_current_user),
):
    if not current_user.success:
        return {"success": False, "message": current_user.message}

    return crud.get_log_details(db, inspection_id)


@router.put("/detail/{detail_id}")
def update_log_detail_validity(
    detail_id: int,
    is_valid: InspectionDetailUpdateValidity = Body(),
    db: Session = Depends(deps.get_db),
    current_user: UserReadResponse = Depends(deps.get_current_user),
):
    if not current_user.success:
        return {"success": False, "message": current_user.message}

    return crud.update_log_detail_validity(db, detail_id, is_valid)
