from sqlalchemy.orm import Session
from app.models.rank import Rank


def create_rank(db: Session, id: int, rank: str):
    rank = Rank(id=id, rank=rank)
    db.add(rank)
    db.commit()
    db.refresh(rank)
    return rank
