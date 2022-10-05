from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional


class BaseAccessBase(BaseModel):
    success: Optional[bool] = Field(None, description="성공여부")
    message: Optional[str] = Field(None, description="실행결과")
    base_name: str = Field(None, description="부대명/위병소명")
    access_time: datetime = Field(None, description="출입시각")
    image: bytes = Field(None, description="출입 사진")


class BaseAccessCreate(BaseAccessBase):
    pass


class BaseAccessRead(BaseAccessBase):
    class Config:
        orm_mode = True
