from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.crud import appearance as crud
from app.schemas import appearance as schema
from app.api import deps


router = APIRouter()


@router.get("/", response_model=List[schema.AppearanceRead])
def get_appearances(db: Session = Depends(deps.get_db)):
    return crud.get_appearances(db)
