from typing import Optional
from pydantic import Field
from app.db.base_schema import Response


class TokenResponse(Response):
    access_token: Optional[str] = Field(None, description="access token")

    class Config:
        schema_extra = {
            "example": {
                "success": True,
                "message": "success",
                "access_token": "jwt token",
            }
        }
