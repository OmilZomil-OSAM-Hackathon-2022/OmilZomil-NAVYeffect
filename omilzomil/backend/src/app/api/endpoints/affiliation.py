from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.crud import affiliation as crud
from app.schemas import affiliation as schema
from app.api import deps


router = APIRouter()


@router.get("/", response_model=List[schema.AffiliationRead])
def get_affiliations(db: Session = Depends(deps.get_db)):
    return crud.get_affiliations(db)
