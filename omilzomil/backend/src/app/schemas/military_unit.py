from pydantic import BaseModel, Field
from typing import Optional
from app.db.base_schema import Response, AllOptional


class MilitaryUnitBase(BaseModel):
    unit: str = Field(None, description="unit name")

    class Config:
        schema_extra = {
            "example": {
                "unit": "계룡대 근무지원단 본부대대",
            }
        }


class MilitaryUnitCreate(MilitaryUnitBase):
    pass


class MilitaryUnitRead(MilitaryUnitBase):
    unit_id: int = Field(None, description="unit id")

    class Config:
        schema_extra = {
            "example": {
                "unit_id": 1,
                "unit": "계룡대 근무지원단 본부대대",
            }
        }
        orm_mode = True


class MilitaryUnitReadResponse(MilitaryUnitRead, metaclass=AllOptional):
    success: Optional[bool] = Field(None, description="result")
    message: Optional[str] = Field(None, description="message")

    class Config:
        schema_extra = {
            "example": {
                "success": True,
                "message": "success",
                "unit_id": 1,
                "unit": "계룡대 근무지원단 본부대대",
            }
        }


class MilitaryUnitUpdate(MilitaryUnitBase):
    pass


class MilitaryUnitResponse(Response):
    pass
