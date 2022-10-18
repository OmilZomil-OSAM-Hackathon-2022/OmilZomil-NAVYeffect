from pydantic import BaseModel, Field
from typing import Optional
from app.db.base_schema import Response, AllOptional
from app.schemas.guardhouse import GuardhouseRead


class UnitHouseRelationBase(BaseModel):
    house_id: int = Field(None, description="guardhouse id")

    class Config:
        schema_extra = {
            "example": {
                "house_id": 1,
            }
        }


class UnitHouseRelationCreate(UnitHouseRelationBase):
    pass


class UnitHouseRelationRead(GuardhouseRead):
    pass


class UnitHouseRelationResponse(Response):
    pass


class UnitHouseRelationReadResponse(UnitHouseRelationRead, metaclass=AllOptional):
    success: Optional[bool] = Field(None, description="result")
    message: Optional[str] = Field(None, description="message")

    class Config:
        schema_extra = {
            "example": {
                "success": True,
                "message": "success",
                "house_id": 1,
                "house": "계룡대 1정문",
            }
        }
