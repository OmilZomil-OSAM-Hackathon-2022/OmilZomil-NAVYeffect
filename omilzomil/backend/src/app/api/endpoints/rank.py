from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.crud import rank as crud
from app.schemas import rank as schema
from app.api import deps


router = APIRouter()


@router.get("/", response_model=List[schema.RankRead])
def get_ranks(db: Session = Depends(deps.get_db)):
    return crud.get_ranks(db)
