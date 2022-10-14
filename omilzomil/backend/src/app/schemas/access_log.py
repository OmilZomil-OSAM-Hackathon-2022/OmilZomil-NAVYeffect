from datetime import datetime
from pydantic import BaseModel, Field


class AccessLogBase(BaseModel):
    military_base: str = Field(None, description="military base")
    access_time: datetime = Field(None, description="access time")
    image_path: bytes = Field(None, description="image path")


class AccessLogCreate(AccessLogBase):
    pass


class AccessLogRead(AccessLogBase):
    class Config:
        schema_extra = {
            "example": {
                "military_base": "계룡대 1정문",
                "access_time": datetime.now(),
                "image_path": "image path",
            }
        }
        orm_mode = True
