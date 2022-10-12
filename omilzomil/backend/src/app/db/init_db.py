from sqlalchemy.orm import Session
from app.db.session import engine
from app.models.rank import Base as rank_model
from app.models.affiliation import Base as affiliation_model
from app.models.military_unit import Base as military_unit_model
from app.models.role import Base as role_model
from app.models.user import Base as user_model
from app.models.uniform import Base as uniform_model
from app.models.access_log import Base as access_log_model
from app.models.inspection_log import Base as inspection_log_model
from app.crud import rank as rank_crud
from app.crud import affiliation as affiliation_crud
from app.crud import role as role_crud
from app.crud import uniform as uniform_crud


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

    role_model.metadata.create_all(bind=engine)
    role_crud.create_role(db, "super")
    role_crud.create_role(db, "admin")
    role_crud.create_role(db, "user")
    role_crud.create_role(db, "inactive")

    user_model.metadata.create_all(bind=engine)

    military_unit_model.metadata.create_all(bind=engine)

    uniform_model.metadata.create_all(bind=engine)
    uniform_crud.create_uniform(db, "샘당")
    uniform_crud.create_uniform(db, "정복")
    uniform_crud.create_uniform(db, "군복")

    access_log_model.metadata.create_all(bind=engine)
    inspection_log_model.metadata.create_all(bind=engine)
