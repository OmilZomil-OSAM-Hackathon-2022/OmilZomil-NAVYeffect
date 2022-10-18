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
