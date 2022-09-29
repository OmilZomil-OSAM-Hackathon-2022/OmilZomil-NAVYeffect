from typing import Optional
from pydantic import BaseModel, Field


from core.base_schema import AllOptional

# Shared properties
class CameraBase(BaseModel):
    name: str = Field(title="카메라 이름", description='카메라 식별 이름')
    pos: str = Field(title="위치", description='해당 카메라가 존재하는 위치')
    

# Properties to receive on item creation
class CameraCreate(CameraBase):

    class Config:
        schema_extra = {
            "example": {
                "name": "1정문 카메라",
                "uid": "계룡대",
            }
        }
    

# Properties to receive on item update
class CameraUpdate(CameraBase, metaclass=AllOptional):
    permission: int

    pass

class CameraDisplay(CameraBase):
    id: int

    class Config:
        orm_mode = True
