from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api import deps
from app.crud import test as crud


router = APIRouter()


@router.post("/")
async def create_test_case(db: Session = Depends(deps.get_db)):
    return crud.create_test_case(db)
