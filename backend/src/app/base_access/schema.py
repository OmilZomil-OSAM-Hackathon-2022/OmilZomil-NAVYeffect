from datetime import datetime
from pydantic import BaseModel, Field
from core.base_schema import AllOptional


# Shared Properties
class BaseAccessSchema(BaseModel):
    base_name: str = Field(title="부대명/위병소명", description="str 형식의 출입이 기록된 부대/위병소 이름")
    access_time: datetime = Field(title="출입시각", description="DateTime 형식의 출입시각")
    image: bytes = Field(title="출입 사진", description="bytes 형식의 base64 인코딩 된 출입 사진")


# Properties to receive on item creation
class BaseAccessCreate(BaseAccessSchema):
    class Config:
        schema_extra = {
            "example": {
                "base_name": "계룡대 1정문",
                "access_time": datetime(2023, 4, 22, 9, 0),
                "image": b"iVBORw0KGgoAAAANSUhEUgAAAAEAAAABAQMAAAAl21bKAAAAA1BMVEUAAACnej3aAAAAAXRSTlMAQObYZgAAAApJREFUCNdjYAAAAAIAAeIhvDMAAAAASUVORK5CYII=",
            }
        }


# Properties to receive on item update
class BaseAccessRead(BaseAccessSchema):
    class Config:
        orm_mode = True


class BaseAccessUpdate(BaseAccessSchema, metaclass=AllOptional):
    pass
