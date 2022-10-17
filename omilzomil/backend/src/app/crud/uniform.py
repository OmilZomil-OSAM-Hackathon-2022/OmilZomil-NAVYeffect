from sqlalchemy.orm import Session
from app.models.uniform import Uniform


def create_uniform(db: Session, uniform_id: int, uniform: str):
    uniform = Uniform(uniform_id=uniform_id, uniform=uniform)
    db.add(uniform)
    db.commit()
    db.refresh(uniform)
    return uniform


def get_uniforms(db: Session):
    return db.query(Uniform).filter(Uniform.uniform_id != 1).all()
