from sqlalchemy.orm import Session


from app.user.model import User
from app.user.schema import UserCreate
from app.token.jwt import get_password_hash

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()

def get_user_by_uid(db: Session, uid: int):
    return db.query(User).filter(User.uid == uid).first()

def create_user(db: Session, user: UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = User(
        name=user.name, 
        uid=user.uid, 
        password=hashed_password, 
        dog_num=user.dog_num,
        rank=user.rank,
        army=user.army,
        unit=user.unit,
        disable=False
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
7