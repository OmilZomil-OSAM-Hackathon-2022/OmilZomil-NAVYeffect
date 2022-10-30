from fastapi import APIRouter, Depends
from fastapi_pagination import paginate
from sqlalchemy.orm import Session
from app.api import deps
from app.crud import statistics as crud
from app.schemas.CustomParams import CustomParams


router = APIRouter()


@router.get("/")
async def get_rankings(params: CustomParams = Depends(), db: Session = Depends(deps.get_db)):
    return paginate(crud.get_monthly_unit_ranks(db), params)
