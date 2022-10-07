from sqlalchemy.orm import Session
from app.db.session import engine
from app.models.rank import Base as rank_model
from app.models.affiliation import Base as affiliation_model
from app.models.military_unit import Base as military_unit_model
from app.models.base_access import Base as base_access_model
from app.models.enlisted_personnel import Base as enlisted_personnel_model
from app.crud import rank as rank_crud
from app.crud import affiliation as affiliation_crud


def init_db(db: Session):
    rank_model.metadata.create_all(bind=engine)
    rank_crud.create_rank(db, "이등병")
    rank_crud.create_rank(db, "일등병")
    rank_crud.create_rank(db, "상등병")
    rank_crud.create_rank(db, "병장")

    affiliation_model.metadata.create_all(bind=engine)
    affiliation_crud.create_affiliation(db, "육군")
    affiliation_crud.create_affiliation(db, "해군")
    affiliation_crud.create_affiliation(db, "공군")
    affiliation_crud.create_affiliation(db, "해병대")
    affiliation_crud.create_affiliation(db, "국방부직할")

    military_unit_model.metadata.create_all(bind=engine)

    base_access_model.metadata.create_all(bind=engine)
    enlisted_personnel_model.metadata.create_all(bind=engine)
