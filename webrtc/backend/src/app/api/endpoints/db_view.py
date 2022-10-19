from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from omil.app.schemas import rank as rank_schemas
from app.models.rank import Rank
from app.api import deps


router = APIRouter()


@router.get("/rank", response_model=List[rank_schemas.RankRead])
def get_ranks(db: Session = Depends(deps.get_db)):
    """
    정상적으로 데이터가 들어갔는지 조회
    """
    model_list = db.query(Rank).order_by(Rank.rank_id).all()
    return model_list
