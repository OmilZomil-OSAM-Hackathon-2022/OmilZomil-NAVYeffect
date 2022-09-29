from sqlalchemy.orm import Session

from app.camera.model import User
from app.camera.schema import UserCreate

def get_camera(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()

def get_camera_by_name(db: Session, name: int):
    return db.query(User).filter(User.uid == uid).first()

def create_user(db: Session, user: UserCreate):
    hashed_password = get_password_haash(user.password)
    db_user = User(
        name=user.name, 
        uid=user.uid, 
        password=hashed_password, 
        dog_num=user.dog_num,
        rank=user.rank,
        army=user.army,
        unit=user.unit,
        permission=4
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
7