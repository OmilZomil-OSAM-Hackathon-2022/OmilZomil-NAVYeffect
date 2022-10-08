from pydantic import BaseModel, Field
from typing import Optional


class MilitaryUnitBase(BaseModel):
    success: Optional[bool] = Field(None, description="result")
    message: Optional[str] = Field(None, description="message")
    unit: str = Field(None, description="unit name")

    class Config:
        schema_extra = {
            "example": {
                "unit": "계룡대 근무지원단",
            }
        }


class MilitaryUnitCreate(MilitaryUnitBase):
    pass


class MilitaryUnitRead(MilitaryUnitBase):
    class Config:
        orm_mode = True


class MilitaryUnitUpdate(MilitaryUnitBase):
    pass


class MilitaryUnitDelete(MilitaryUnitBase):
    pass
