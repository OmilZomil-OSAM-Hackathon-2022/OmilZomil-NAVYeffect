from sqlalchemy.orm import Session
from app.db.session import engine
from app.models.rank import Base as rank_model
from app.models.base_access import Base as base_access_model
from app.models.enlisted_personnel import Base as enlisted_personnel_model
from app.crud import rank as rank_crud


def init_db(db: Session):
    rank_model.metadata.create_all(bind=engine)
    rank_crud.create_rank(db, "이등병")
    rank_crud.create_rank(db, "일등병")
    rank_crud.create_rank(db, "상등병")
    rank_crud.create_rank(db, "병장")

    base_access_model.metadata.create_all(bind=engine)
    enlisted_personnel_model.metadata.create_all(bind=engine)
