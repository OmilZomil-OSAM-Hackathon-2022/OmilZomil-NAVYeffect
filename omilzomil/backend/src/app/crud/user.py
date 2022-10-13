import sqlalchemy.exc
from sqlalchemy.orm import Session
from app.core.security import get_password_hash, verify_password
from app.models.role import Role
from app.models.user import User
from app.schemas.user import UserCreate, UserFilter, UserUpdateInformation, UserUpdatePassword, UserUpdateRole, UserResponse


def create_user(db: Session, user: UserCreate):
    try:
        user = User(
            full_name=user.full_name,
            dog_number=user.dog_number,
            affiliation=user.affiliation,
            military_unit=user.military_unit,
            rank=user.rank,
            username=user.username,
            password=get_password_hash(user.password),
        )
        db.add(user)
        db.commit()
        db.refresh(user)
        return UserResponse(success=True, message="success")
    except sqlalchemy.exc.IntegrityError as e:
        if "foreign key constraint fail" in e.orig.args[1]:
            return UserResponse(success=False, message="foreign key constraint fail")
        elif "Duplicate entry" in e.orig.args[1]:
            return UserResponse(success=False, message="unique key constraint fail")
        raise e


def get_user(db: Session, flt: UserFilter):
    is_active = flt.is_active
    flt = {x: (y is None and "%" or f"%{y}%") for x, y in flt.dict().items() if x != "is_active"}

    user = (
        db.query(User)
        .filter(User.full_name.like(flt["full_name"]))
        .filter(User.affiliation.like(flt["affiliation"]))
        .filter(User.military_unit.like(flt["military_unit"]))
        .filter(User.rank.like(flt["rank"]))
    )

    if is_active is not None:
        if is_active:
            user = user.filter(User.role != "inactive")
        else:
            user = user.filter(User.role == "inactive")

    return user.all()


def update_user_information(db: Session, user_id: int, information: UserUpdateInformation):
    user = db.query(User).filter_by(user_id=user_id)
    if not user.count():
        return UserResponse(success=False, message="entry not found")
    try:
        user.update(information.dict())
        db.commit()
        return UserResponse(success=True, message="success")
    except sqlalchemy.exc.IntegrityError as e:
        if "foreign key constraint fail" in e.orig.args[1]:
            return UserResponse(success=False, message="foreign key constraint fail")
        elif "Duplicate entry" in e.orig.args[1]:
            return UserResponse(success=False, message="unique key constraint fail")
        raise e


def update_user_password(db: Session, user_id: int, password: UserUpdatePassword):
    user = db.query(User).filter_by(user_id=user_id)
    if not user.count():
        return UserResponse(success=False, message="entry not found")

    if not verify_password(password.old_password, user.first().password):
        return UserResponse(success=False, message="invalid password")

    user.update({"password": get_password_hash(password.new_password)})
    db.commit()
    return UserResponse(success=True, message="success")


def update_user_role(db: Session, user_id: int, role: UserUpdateRole):
    user = db.query(User).filter_by(user_id=user_id)
    if not user.count():
        return UserResponse(success=False, message="entry not found")
    try:
        user.update(role.dict())
        db.commit()
        return UserResponse(success=True, message="success")
    except sqlalchemy.exc.IntegrityError:
        return UserResponse(success=False, message="foreign key constraint fail")


def authenticate(db: Session, *, username: str, password: str):
    user = db.query(User).filter_by(username=username)
    if not user.count():
        return None

    user = user.first()
    if not verify_password(password, user.password):
        return None

    return user


def is_active(db: Session, user: User):
    try:
        role = db.query(Role).filter_by(role_id=user.role).first()
        return role.role != "inactive"
    except Exception:
        return None
