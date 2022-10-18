from typing import List
from fastapi import APIRouter, Depends, Body
from sqlalchemy.orm import Session
from app.crud import vacation as crud
from app.schemas import vacation as schema
from app.api import deps


router = APIRouter()


@router.post("/{user_id}", response_model=schema.VacationResponse)
async def create_vacation(user_id: int, vacation: schema.VacationCreate = Body(), db: Session = Depends(deps.get_db)):
    return crud.create_vacation(db, user_id, vacation)


@router.get("/{user_id}", response_model=List[schema.VacationRead])
def get_vacations(user_id: int, db: Session = Depends(deps.get_db)):
    return crud.get_vacations(db, user_id)


@router.put("/confirm/{user_id}/{vacation_id}", response_model=schema.VacationResponse)
async def update_vacation_confirmation(
    user_id: int, vacation_id: int, confirmed: schema.VacationUpdateConfirmation = Body(), db: Session = Depends(deps.get_db)
):
    return crud.update_vacation_confirmation(db, vacation_id, confirmed)
