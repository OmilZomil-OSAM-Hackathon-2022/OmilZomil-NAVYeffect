from sqlalchemy.orm import Session
from app.models.role import Role


def create_role(db: Session, role: str):
    role = Role(role=role)
    db.add(role)
    db.commit()
    db.refresh(role)
    return role
