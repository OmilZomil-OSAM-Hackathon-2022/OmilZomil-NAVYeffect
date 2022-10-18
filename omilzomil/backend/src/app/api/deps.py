from typing import Generator
from fastapi import Depends
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
        return UserReadResponse(success=False, message="invalid credentials")
    return crud.get_user(db, user_id=user_id)


def get_current_active_user(current_user: UserReadResponse = Depends(get_current_user)):
    if current_user.role == "inactive":
        return UserReadResponse(success=False, message="inactive user")
    return current_user


def get_current_active_superuser(current_user: UserReadResponse = Depends(get_current_user)):
    if current_user.role != "super":
        return UserReadResponse(success=False, message="not enough privileges")
    return current_user
