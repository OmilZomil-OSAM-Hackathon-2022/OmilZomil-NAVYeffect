from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.crud import uniform as crud
from app.schemas import uniform as schema
from app.api import deps


router = APIRouter()


@router.get("/", response_model=List[schema.UniformRead])
def get_uniforms(db: Session = Depends(deps.get_db)):
    return crud.get_uniforms(db)
