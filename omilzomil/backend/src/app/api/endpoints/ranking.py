from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api import deps
from app.crud import statistics as crud


router = APIRouter()


@router.get("/")
def get_rankings(page: int = 1, db: Session = Depends(deps.get_db)):
    return crud.get_monthly_unit_ranks(db, page)
