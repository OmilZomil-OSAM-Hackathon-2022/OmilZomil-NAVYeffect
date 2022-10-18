from sqlalchemy.orm import Session
from app.db.session import engine
from app.models.affiliation import Base as affiliation_model
from app.models.military_unit import Base as military_unit_model
from app.models.rank import Base as rank_model
from app.models.role import Base as role_model
from app.models.user import Base as user_model
from app.models.vacation import Base as vacation_model
from app.models.guardhouse import Base as guardhouse_model
from app.models.unit_house_relation import Base as unit_house_relation_model
from app.models.uniform import Base as uniform_model
from app.models.inspection_log import Base as inspection_log_model
from app.models.appearance import Base as appearance_model
from app.models.inspection_detail import Base as inspection_detail_model
from app.crud import affiliation as affiliation_crud
from app.crud import military_unit as military_unit_crud
from app.crud import rank as rank_crud
from app.crud import role as role_crud
from app.crud import user as user_crud
from app.crud import uniform as uniform_crud
from app.crud import appearance as appearance_crud


def init_db(db: Session):
    affiliation_model.metadata.create_all(bind=engine)
    affiliation_crud.create_affiliation(db, 1, "unknown")
    affiliation_crud.create_affiliation(db, 2, "육군")
    affiliation_crud.create_affiliation(db, 3, "해군")
    affiliation_crud.create_affiliation(db, 4, "공군")
    affiliation_crud.create_affiliation(db, 5, "해병대")

    military_unit_model.metadata.create_all(bind=engine)
    military_unit_crud.create_military_unit(db, unit_id=1, unit="unknown")

    rank_model.metadata.create_all(bind=engine)
    rank_crud.create_rank(db, 1, "unknown")
    rank_crud.create_rank(db, 2, "이병")
    rank_crud.create_rank(db, 3, "일병")
    rank_crud.create_rank(db, 4, "상병")
    rank_crud.create_rank(db, 5, "병장")

    role_model.metadata.create_all(bind=engine)
    role_crud.create_role(db, 1, "user")
    role_crud.create_role(db, 2, "admin")
    role_crud.create_role(db, 3, "super")

    user_model.metadata.create_all(bind=engine)
    user_crud.create_super_admin(db, "super", "super")

    vacation_model.metadata.create_all(bind=engine)

    guardhouse_model.metadata.create_all(bind=engine)
    unit_house_relation_model.metadata.create_all(bind=engine)

    uniform_model.metadata.create_all(bind=engine)
    uniform_crud.create_uniform(db, 1, "unknown")
    uniform_crud.create_uniform(db, 2, "샘당")
    uniform_crud.create_uniform(db, 3, "정복")
    uniform_crud.create_uniform(db, 4, "군복")

    inspection_log_model.metadata.create_all(bind=engine)

    appearance_model.metadata.create_all(bind=engine)
    appearance_crud.create_appearance(db, 1, "두발")
    appearance_crud.create_appearance(db, 2, "이름표")
    appearance_crud.create_appearance(db, 3, "계급장")
    appearance_crud.create_appearance(db, 4, "태극기")
    appearance_crud.create_appearance(db, 5, "모자")
    appearance_crud.create_appearance(db, 6, "네커치프")
    appearance_crud.create_appearance(db, 7, "머플러")

    inspection_detail_model.metadata.create_all(bind=engine)
