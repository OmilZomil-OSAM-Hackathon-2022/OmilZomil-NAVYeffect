from datetime import datetime
from pydantic import BaseModel, Field


class AccessLogBase(BaseModel):
    military_base: str = Field(None, description="military base")
    access_time: datetime = Field(None, description="access time")
    image: bytes = Field(None, description="base64 encoded image")


class AccessLogCreate(AccessLogBase):
    pass


class AccessLogRead(AccessLogBase):
    class Config:
        schema_extra = {
            "example": {
                "military_base": "계룡대 1정문",
                "access_time": datetime.now(),
                "image": b"base64_encoded_image",
            }
        }
        orm_mode = True
