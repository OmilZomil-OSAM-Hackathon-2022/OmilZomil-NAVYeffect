from dateutil.relativedelta import relativedelta
from typing import Optional
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api import deps
from app.schemas.user import UserReadResponse
from app.schemas.statistics import Date
from app.crud import statistics as crud


router = APIRouter()


@router.post("/test-case")
def create_test_case(db: Session = Depends(deps.get_db)):
    return crud.create_test_case(db)


@router.get("/month/fail/")
def get_monthly_fail(db: Session = Depends(deps.get_db)):
    cur = Date.now(day=False)
    prev = cur - relativedelta(months=1)

    total, cur = crud.get_overall_stats(db, date=cur, status=False)
    _, prev = crud.get_overall_stats(db, date=prev, status=False)

    if cur != 0:
        fail_rate = round((cur / total) * 100)
    else:
        fail_rate = 0

    if prev != 0:
        increase_rate = round(((cur / prev) - 1) * 100)
    else:
        increase_rate = 0

    return {"success": True, "message": "success", "count": cur, "fail_rate": fail_rate, "increase_rate": increase_rate}


@router.get("/month/fail/affiliation/")
def get_afiiliation_monthly_fail(db: Session = Depends(deps.get_db)):
    counts = list()
    for i in range(2, 6):
        _, count = crud.get_overall_stats(db, date=Date.now(day=False), affiliation=i, status=False)
        counts.append(count)

    total = sum(counts)
    affiliations = ["육군", "해군", "공군", "해병대"]

    if total == 0:
        ret = {affiliations[i]: 0 for i in range(0, len(affiliations))}
        ret.update({"success": False, "message": "failure entry not found"})
    else:
        counts = [round(counts[i] / total * 100) for i in range(0, len(counts))]
        if sum(counts) != 100:
            counts[3] += 100 - sum(counts)

        ret = {affiliations[i]: counts[i] for i in range(0, len(affiliations))}
        ret.update({"success": True, "message": "success"})

    return ret


@router.get("/month/fail/detail/")
def get_detailed_monthly_fail(db: Session = Depends(deps.get_db)):
    ret = {"success": True, "message": "success"}
    types = {"두발": 1, "이름표": 2, "계급장": 3, "태극기": 4, "모자": 5}

    for appearance_type in types.items():
        total, count = crud.get_overall_stats(
            db,
            date=Date.now(day=False),
            appearance_type=appearance_type[1],
            status=False,
        )

        if total != 0:
            ret[appearance_type[0]] = round(count / total * 100)
        else:
            ret[appearance_type[0]] = 0

    return ret


@router.get("/year/fail/")
def get_yearly_fail(db: Session = Depends(deps.get_db)):
    ret = {"success": True, "message": "success"}

    cur = Date.now(day=False)
    for i in range(0, 12):
        date = cur - relativedelta(months=i)
        total, count = crud.get_overall_stats(db, date=date, status=False)
        if total != 0:
            ret[str(date)] = round(count / total * 100)
        else:
            ret[str(date)] = 0

    return ret


@router.get("/month/unit/")
def get_monthly_data_from_unit(
    category: Optional[str] = None, db: Session = Depends(deps.get_db), current_user: UserReadResponse = Depends(deps.get_current_user)
):
    if not current_user.success:
        return {"success": False, "message": current_user.message}

    status = None
    if category == "hair" or category == "appearance":
        status = True
    elif category is not None:
        return {"success": False, "message": "invalid category"}

    cur = Date.now(day=False)
    prev = cur - relativedelta(months=1)

    _, cur = crud.get_overall_stats(db, date=cur, military_unit=current_user.military_unit, category=category, status=status)
    _, prev = crud.get_overall_stats(db, date=prev, military_unit=current_user.military_unit, category=category, status=status)

    if prev != 0:
        increase_rate = round(((cur / prev) - 1) * 100)
    else:
        increase_rate = 0

    return {"success": True, "message": "success", "count": cur, "increase_rate": increase_rate}


@router.get("/month/unit/fail/detail/")
def get_detailed_monthly_fail_from_unit(db: Session = Depends(deps.get_db), current_user: UserReadResponse = Depends(deps.get_current_user)):
    if not current_user.success:
        return {"success": False, "message": current_user.message}

    ret = {"success": True, "message": "success"}
    types = {"이름표": 2, "계급장": 3, "태극기": 4, "모자": 5}

    for appearance_type in types.items():
        _, count = crud.get_overall_stats(
            db,
            date=Date.now(day=False),
            military_unit=current_user.military_unit,
            appearance_type=appearance_type[1],
            status=False,
        )
        ret[appearance_type[0]] = count

    return ret


@router.get("/month/unit/pass/")
def get_monthly_pass_from_unit(db: Session = Depends(deps.get_db), current_user: UserReadResponse = Depends(deps.get_current_user)):
    if not current_user.success:
        return {"success": False, "message": current_user.message}

    ret = {"success": True, "message": "success"}

    cur = Date.now(day=False)
    for i in range(0, 12):
        date = cur - relativedelta(months=i)
        total, count = crud.get_overall_stats(db, date=date, military_unit=current_user.military_unit, status=True)
        if total != 0:
            ret[str(date)] = round(count / total * 100)
        else:
            ret[str(date)] = 0

    return ret


@router.get("/month/unit/best/{category}")
def get_monthly_best_from_unit(category: str, db: Session = Depends(deps.get_db), current_user: UserReadResponse = Depends(deps.get_current_user)):
    if not current_user.success:
        return {"success": False, "message": current_user.message}

    if not (category == "unit" or category == "person"):
        return {"success": False, "message": "invalid category"}

    ret = {"success": True, "message": "success"}
    ret.update(crud.get_monthly_best_stats(db, military_unit=current_user.military_unit, category=category))
    return ret
