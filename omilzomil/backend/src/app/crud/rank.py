from sqlalchemy.orm import Session
from app.models.rank import Rank


def create_rank(db: Session, rank_id: int, rank: str):
    rank = Rank(rank_id=rank_id, rank=rank)
    db.add(rank)
    db.commit()
    db.refresh(rank)
    return rank
