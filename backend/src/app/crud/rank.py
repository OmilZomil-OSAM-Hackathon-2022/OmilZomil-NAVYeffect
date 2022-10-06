from sqlalchemy.orm import Session
from app.models.rank import Rank


def create_rank(db: Session, rank: str):
    rank = Rank(rank=rank.rank)
    db.add(rank)
    db.commit()
    db.refresh(rank)
    return rank
