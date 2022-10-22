from fastapi import APIRouter, Depends
from fastapi_pagination import paginate, Params
from sqlalchemy.orm import Session
from app.api import deps
from app.crud import statistics as crud


router = APIRouter()


@router.get("/")
async def get_rankings(db: Session = Depends(deps.get_db), params: Params = Depends()):
    return paginate(crud.get_monthly_unit_ranks(db), params)
