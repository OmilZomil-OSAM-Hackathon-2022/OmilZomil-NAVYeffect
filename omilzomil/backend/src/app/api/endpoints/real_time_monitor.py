from datetime import date
from typing import Optional
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.user import UserReadResponse
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
