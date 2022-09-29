from sqlalchemy.orm import Session

from app.camera.model import Camera
from app.camera.schema import CameraCreate

def get_camera(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Camera).offset(skip).limit(limit).all()

def get_camera_by_uid(db: Session, name: int):
    return db.query(Camera).filter(Camera.uid == uid).first()

def create_camera(db: Session, camera: CameraCreate):
    hashed_password = get_password_haash(camera.password)
    db_camera = Camera(
        name=camera.name, 
        uid=camera.uid, 
        pos=camera.pos, 
    )
    db.add(db_camera)
    db.commit()
    db.refresh(db_camera)
    return db_camera
