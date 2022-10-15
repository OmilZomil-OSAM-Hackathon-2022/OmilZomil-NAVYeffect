from datetime import datetime
from dateutil.relativedelta import relativedelta
from typing import Optional
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api import deps
from app.schemas.user import UserReadResponse
from app.crud import statistics as crud


router = APIRouter()


@router.get("/unit/rate/")
def get_rate_from_unit(category: Optional[str] = None, db: Session = Depends(deps.get_db), current_user: UserReadResponse = Depends(deps.get_current_user)):
    if not current_user.success:
        return {"success": False, "message": current_user.message}

    status = None
    if category == "hair" or category == "appearance":
        status = True
    elif category is not None:
        return {"success": False, "message": "invalid category"}

    cur = datetime.now()
    prev = cur - relativedelta(months=1)

    cur = crud.get_monthly_overall_stats(db, military_unit=current_user.military_unit, category=category, status=status)
    prev = crud.get_monthly_overall_stats(db, military_unit=current_user.military_unit, date=prev, category=category, status=status)

    if prev != 0:
        increase_rate = ((cur / prev) - 1) * 100
    else:
        increase_rate = 0

    return {"success": True, "message": "success", "count": cur, "increase_rate": increase_rate}


@router.get("/unit/fail/")
def get_fail_from_unit(db: Session = Depends(deps.get_db), current_user: UserReadResponse = Depends(deps.get_current_user)):
    if not current_user.success:
        return {"success": False, "message": current_user.message}

    ret = {"success": True, "message": "success"}
    types = {"이름표": 2, "계급장": 3, "태극기": 4, "모자": 5}

    for appearance_type in types.items():
        ret[appearance_type[0]] = crud.get_monthly_detailed_stats(db, military_unit=current_user.military_unit, appearance_type=appearance_type[1], status=True)

    return ret


@router.get("/unit/pass/")
def get_pass_from_unit(db: Session = Depends(deps.get_db), current_user: UserReadResponse = Depends(deps.get_current_user)):
    if not current_user.success:
        return {"success": False, "message": current_user.message}

    ret = {"success": True, "message": "success"}

    cur = datetime.now()
    for i in range(0, 12):
        date = cur - relativedelta(months=i)
        ret[date.strftime("%Y-%m")] = crud.get_monthly_overall_stats(db, military_unit=current_user.military_unit, date=date, status=True)

    return ret
