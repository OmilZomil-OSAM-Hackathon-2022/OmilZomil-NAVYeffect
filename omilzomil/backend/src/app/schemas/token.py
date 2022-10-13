from typing import Optional
from pydantic import BaseModel, Field
from app.db.base_schema import Response
from app.schemas.user import UserRead


class TokenResponse(Response):
    access_token: Optional[str] = Field(None, description="access token")


class TokenPayload(BaseModel):
    sub: Optional[int] = Field(None, description="sub")
