from typing import Generator
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from pydantic import ValidationError
from sqlalchemy.orm import Session
from app.core import security
from app.core.config import settings
from app.crud import user as crud
from app.schemas.user import UserReadResponse
from app.db.session import SessionLocal


reusable_oauth2 = OAuth2PasswordBearer(tokenUrl="/login/access-token")


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def get_current_user(db: Session = Depends(get_db), token: str = Depends(reusable_oauth2)):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[security.ALGORITHM])
        user_id = payload["sub"]
    except (jwt.JWTError, ValidationError):
        return UserReadResponse(success=False, message="could not validate credentials")
    user = crud.get_user_by_id(db, user_id=user_id)
    if not user:
        return UserReadResponse(success=False, message="user not found")

    user = UserReadResponse(
        success=True,
        message="success",
        user_id=user.user_id,
        full_name=user.full_name,
        dog_number=user.dog_number,
        affiliation=user.affiliation,
        military_unit=user.military_unit,
        rank=user.rank,
        username=user.username,
        role=user.role,
    )
    return user


def get_current_active_user(current_user: UserReadResponse = Depends(get_current_user)):
    if not crud.is_active(current_user):
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


def get_current_active_superuser(current_user: UserReadResponse = Depends(get_current_user)):
    if not crud.is_superuser(current_user):
        raise HTTPException(status_code=400, detail="The user doesn't have enough privileges")
    return current_user
