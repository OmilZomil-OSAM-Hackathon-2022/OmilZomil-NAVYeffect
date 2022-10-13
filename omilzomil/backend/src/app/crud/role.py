from sqlalchemy.orm import Session
from app.models.role import Role


def create_role(db: Session, role_id: int, role: str):
    role = Role(rold_id=role_id, role=role)
    db.add(role)
    db.commit()
    db.refresh(role)
    return role
