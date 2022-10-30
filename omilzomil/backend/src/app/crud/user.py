import sqlalchemy.exc
from sqlalchemy.orm import Session
from app.core.security import get_password_hash, verify_password
from app.models.user import User
from app.schemas.user import (
    UserCreate,
    UserFilter,
    UserUpdateInformation,
    UserUpdatePassword,
    UserUpdateRole,
    UserUpdateActivity,
    UserDelete,
    UserResponse,
    UserReadResponse,
)


def create_super_admin(db: Session, username: str, password: str):
    user = User(
        full_name="super admin",
        dog_number="super admin",
        affiliation=1,
        military_unit=1,
        rank=1,
        username=username,
        password=get_password_hash(password),
        role=3,
        is_active=True,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return UserResponse(success=True, message=user.user_id)


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
        return UserResponse(success=True, message=user.user_id)
    except sqlalchemy.exc.IntegrityError as e:
        msg = e.orig.args[1]
        if "foreign key constraint fail" in msg:
            return UserResponse(success=False, message="foreign key constraint fail")
        elif "Duplicate entry" in msg:
            msg = msg.split("'")[3].split(".")[1]
            if "dog_number" == msg or "username" == msg:
                return UserResponse(success=False, message=f"unique key constraint fail in {msg}")
        raise e


def get_users(db: Session, flt: UserFilter):
    user = db.query(User).filter(User.user_id != 1)
    if flt.full_name is not None:
        user = user.filter(User.full_name.like(f"%{flt.full_name}%"))
    if flt.affiliation is not None:
        user = user.filter_by(affiliation=flt.affiliation)
    if flt.military_unit is not None:
        user = user.filter_by(military_unit=flt.military_unit)
    if flt.rank is not None:
        user = user.filter_by(rank=flt.rank)
    if flt.is_active is not None:
        user = user.filter_by(is_active=flt.is_active)
    return user.order_by(User.full_name).all()


def get_user(db: Session, user_id: int):
    user = db.query(User).get(user_id)
    if not user:
        return UserReadResponse(success=False, message="entry not found")

    user = UserReadResponse(
        success=True,
        message=user.user_id,
        user_id=user.user_id,
        full_name=user.full_name,
        dog_number=user.dog_number,
        affiliation=user.affiliation,
        military_unit=user.military_unit,
        rank=user.rank,
        username=user.username,
        role=user.role,
        is_active=user.is_active,
    )
    return user


def update_user_information(db: Session, user_id: int, information: UserUpdateInformation):
    user = db.query(User).filter_by(user_id=user_id)
    if not user.count():
        return UserResponse(success=False, message="entry not found")
    try:
        information = {x: y for x, y in information.dict().items() if y is not None}
        user.update(information)
        db.commit()
        return UserResponse(success=True, message=user_id)
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
    return UserResponse(success=True, message=user_id)


def update_user_role(db: Session, user_id: int, role: UserUpdateRole):
    user = db.query(User).filter_by(user_id=user_id)
    if not user.count():
        return UserResponse(success=False, message="entry not found")
    try:
        user.update(role.dict())
        db.commit()
        return UserResponse(success=True, message=user_id)
    except sqlalchemy.exc.IntegrityError:
        return UserResponse(success=False, message="foreign key constraint fail")


def update_user_activity(db: Session, user_id: int, is_active: UserUpdateActivity):
    user = db.query(User).filter_by(user_id=user_id)
    if not user.count():
        return UserResponse(success=False, message="entry not found")
    try:
        user.update(is_active.dict())
        db.commit()
        return UserResponse(success=True, message=user_id)
    except sqlalchemy.exc.IntegrityError:
        return UserResponse(success=False, message="foreign key constraint fail")


def delete_user(db: Session, user_id: int, password: UserDelete):
    user = db.query(User).filter_by(user_id=user_id)
    if not user.count():
        return UserResponse(success=False, message="entry not found")

    if not verify_password(password.password, user.first().password):
        return UserResponse(success=False, message="invalid password")

    user.delete()
    db.commit()
    return UserResponse(success=True, message=user_id)


def authenticate(db: Session, *, username: str, password: str):
    user = db.query(User).filter_by(username=username)
    if not user.count():
        return None

    user = user.first()
    if not verify_password(password, user.password):
        return None

    return user


def is_active(db: Session, user: User):
    return user.is_active is True


def is_super(db: Session, user: User):
    return user.role == 3
