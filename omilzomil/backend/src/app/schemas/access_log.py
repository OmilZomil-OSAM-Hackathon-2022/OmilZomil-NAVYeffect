from datetime import datetime
from pydantic import BaseModel, Field
from app.db.base_schema import Response


class AccessLogBase(BaseModel):
    guardhouse: str = Field(None, description="guardhouse")
    access_time: datetime = Field(None, description="access time")


class AccessLogCreate(AccessLogBase):
    pass


class AccessLogRead(AccessLogBase):
    class Config:
        schema_extra = {
            "example": {
                "guardhouse": "계룡대 1정문",
                "access_time": datetime.now(),
            }
        }
        orm_mode = True


class AccessLogResponse(Response):
    pass
