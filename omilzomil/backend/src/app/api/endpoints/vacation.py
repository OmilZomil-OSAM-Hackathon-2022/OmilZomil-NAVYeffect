from datetime import datetime
from typing import List, Optional
from fastapi import APIRouter, Depends, Body
from sqlalchemy.orm import Session
from app.crud import vacation as crud
from app.schemas.user import UserReadResponse
from app.schemas.military_unit import MilitaryUnitRead
from app.schemas import vacation as schema
from app.api import deps


router = APIRouter()


@router.post("/user/{user_id}", response_model=schema.VacationResponse)
async def create_vacation(user_id: int, vacation: schema.VacationCreate = Body(), db: Session = Depends(deps.get_db)):
    return crud.create_vacation(db, user_id, vacation)


@router.get("/user/{user_id}", response_model=List[schema.VacationRead])
def get_vacations(user_id: int, page: int = 1, db: Session = Depends(deps.get_db)):
    return crud.get_vacations(db, user_id=user_id, page=page)


@router.get("/unit/", response_model=List[schema.VacationRead])
def get_vacations_from_unit(db: Session = Depends(deps.get_db), current_user: UserReadResponse = Depends(deps.get_current_user)):
    return crud.get_vacations(db, unit_id=current_user.military_unit)


@router.get("/name/", response_model=List[MilitaryUnitRead])
def get_unit_names_from_user(
    access_time: datetime,
    affiliation: Optional[int] = None,
    rank: Optional[int] = None,
    name: Optional[str] = None,
    db: Session = Depends(deps.get_db),
):
    return crud.get_unit_names_from_user(db, access_time=access_time, affiliation=affiliation, rank=rank, name=name)


@router.put("/approval/{vacation_id}", response_model=schema.VacationResponse)
async def update_vacation_approval(vacation_id: int, is_approved: schema.VacationUpdateApproval = Body(), db: Session = Depends(deps.get_db)):
    return crud.update_vacation_approval(db, vacation_id, is_approved)


@router.delete("/{vacation_id}", response_model=schema.VacationResponse)
def delete_vacation(vacation_id: int, db: Session = Depends(deps.get_db)):
    return crud.delete_vacation(db, vacation_id)
