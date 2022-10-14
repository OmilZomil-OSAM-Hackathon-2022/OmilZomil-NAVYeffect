from typing import Optional
from pydantic import Field
from app.db.base_schema import Response


class TokenResponse(Response):
    access_token: Optional[str] = Field(None, description="access token")
