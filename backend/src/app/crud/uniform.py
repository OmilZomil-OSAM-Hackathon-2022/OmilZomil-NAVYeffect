from sqlalchemy.orm import Session
from app.models.uniform import Uniform


def create_uniform(db: Session, uniform: str):
    uniform = Uniform(uniform=uniform)
    db.add(uniform)
    db.commit()
    db.refresh(uniform)
    return uniform
