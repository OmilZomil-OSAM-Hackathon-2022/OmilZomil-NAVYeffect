from datetime import date
from typing import Optional
from fastapi import APIRouter, Depends, Body
from sqlalchemy.orm import Session
from app.schemas.user import UserReadResponse
from app.schemas.inspection_log import InspectionLogUpdateInformation, InspectionLogUpdateCheck
from app.schemas.inspection_detail import InspectionDetailUpdateStatus, InspectionDetailUpdateValidity
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
    page: Optional[int] = 1,
    db: Session = Depends(deps.get_db),
    current_user: UserReadResponse = Depends(deps.get_current_active_user),
):
    if not current_user.success:
        return {"success": False, "message": current_user.message}

    return crud.get_logs(
        db, current_user.military_unit, rank=rank, name=name, appearance_type=appearance_type, start_date=start_date, end_date=end_date, page=page
    )


@router.get("/detail/{inspection_id}")
def get_log_details(
    inspection_id: int,
    db: Session = Depends(deps.get_db),
    current_user: UserReadResponse = Depends(deps.get_current_active_user),
):
    if not current_user.success:
        return {"success": False, "message": current_user.message}

    return crud.get_log_details(db, inspection_id)


@router.put("/information/{inspection_id}")
async def update_log_information(
    inspection_id: int,
    information: InspectionLogUpdateInformation = Body(),
    db: Session = Depends(deps.get_db),
    current_user: UserReadResponse = Depends(deps.get_current_active_admin),
):
    if not current_user.success:
        return {"success": False, "message": current_user.message}

    return crud.update_log_information(db, inspection_id, information)


@router.put("/check/{inspection_id}")
async def update_log_check(
    inspection_id: int,
    is_checked: InspectionLogUpdateCheck = Body(),
    db: Session = Depends(deps.get_db),
    current_user: UserReadResponse = Depends(deps.get_current_active_admin),
):
    if not current_user.success:
        return {"success": False, "message": current_user.message}

    return crud.update_log_check(db, inspection_id, is_checked)


@router.put("/detail/status/{detail_id}")
async def update_log_detail_status(
    detail_id: int,
    status: InspectionDetailUpdateStatus = Body(),
    db: Session = Depends(deps.get_db),
    current_user: UserReadResponse = Depends(deps.get_current_active_admin),
):
    if not current_user.success:
        return {"success": False, "message": current_user.message}

    return crud.update_log_detail_status(db, detail_id, status)


@router.put("/detail/validity/{detail_id}")
async def update_log_detail_validity(
    detail_id: int,
    is_valid: InspectionDetailUpdateValidity = Body(),
    db: Session = Depends(deps.get_db),
    current_user: UserReadResponse = Depends(deps.get_current_active_admin),
):
    if not current_user.success:
        return {"success": False, "message": current_user.message}

    return crud.update_log_detail_validity(db, detail_id, is_valid)
