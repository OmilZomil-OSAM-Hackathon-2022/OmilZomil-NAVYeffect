from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.crud import role as crud
from app.schemas import role as schema
from app.api import deps


router = APIRouter()


@router.get("/", response_model=List[schema.RoleRead])
def get_roles(db: Session = Depends(deps.get_db)):
    return crud.get_roles(db)
