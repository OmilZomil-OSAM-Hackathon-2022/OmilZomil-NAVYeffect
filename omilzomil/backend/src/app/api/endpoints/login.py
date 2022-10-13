from typing import Any
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.api import deps
from app.models.user import Base as user_model
from app.schemas import user as user_schema
from app.schemas import token as token_schema
from app.crud import token as token_crud


router = APIRouter()


@router.post("/access-token/", response_model=token_schema.TokenResponse)
def login_access_token(db: Session = Depends(deps.get_db), form_data: OAuth2PasswordRequestForm = Depends()) -> Any:
    return token_crud.create_token(db, form_data.username, form_data.password)


@router.post("/test-token/", response_model=user_schema.UserRead)
def test_token(current_user: user_model = Depends(deps.get_current_user)) -> Any:
    """
    Test access token
    """
    return current_user
