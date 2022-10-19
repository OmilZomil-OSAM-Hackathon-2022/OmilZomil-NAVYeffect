from typing import List
from fastapi import APIRouter, Depends, Body
from sqlalchemy.orm import Session
from app.api import deps

from omil.app.schemas import rank as rank_schemas
from app.models.rank import Rank
from app.models.guardhouse import Guardhouse
from app.schemas import guardhouse as guardhouse_schema
from app.crud import guardhouse as guardhouse_crud



router = APIRouter()


@router.get("/rank", response_model=List[rank_schemas.RankRead])
def get_ranks(db: Session = Depends(deps.get_db)):
    """
    정상적으로 데이터가 들어갔는지 조회
    """
    model_list = db.query(Rank).order_by(Rank.rank_id).all()
    return model_list


@router.get("/guardhouse", response_model=List[guardhouse_schema.GuardhouseRead])
def get_ranks(db: Session = Depends(deps.get_db)):
    """
    위병소 목록이 정상적으로 등록되어 있는지 확인
    """
    model_list =  db.query(Guardhouse).all()
    return model_list

@router.post("/create_guardhouse", response_model=guardhouse_schema.GuardhouseResponse)
async def create_guardhouse(house: guardhouse_schema.GuardhouseCreate = Body(), db: Session = Depends(deps.get_db)):
    """
    위병소를 추가
    """
    return guardhouse_crud.create_guardhouse(db, house.house)