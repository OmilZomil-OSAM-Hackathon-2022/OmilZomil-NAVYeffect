from datetime import timedelta
from sqlalchemy.orm import Session
from app.core import security
from app.core.config import settings
from app.schemas.token import TokenResponse
from app.crud import user as crud


def create_token(db: Session, username: str, password: str):
    user = crud.authenticate(db, username=username, password=password)
    if not user:
        return TokenResponse(success=False, message="incorrect username or password")
    elif not crud.is_active(db, user):
        return TokenResponse(success=False, message="inactive user")

    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    return TokenResponse(success=True, message="success", access_token=security.create_access_token(user.user_id, expires_delta=access_token_expires))
