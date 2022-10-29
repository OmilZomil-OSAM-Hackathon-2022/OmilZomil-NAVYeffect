from pydantic import BaseModel, Field
from typing import Optional
from app.db.base_schema import Response, AllOptional


class GuardhouseBase(BaseModel):
    house: str = Field(None, description="house name")

    class Config:
        schema_extra = {
            "example": {
                "house": "계룡대 1정문",
            }
        }


class GuardhouseCreate(GuardhouseBase):
    pass


class GuardhouseRead(GuardhouseBase):
    house_id: int = Field(None, description="house id")

    class Config:
        schema_extra = {
            "example": {
                "house_id": 1,
                "house": "계룡대 1정문",
            }
        }
        orm_mode = True


class GuardhouseReadResponse(GuardhouseRead, metaclass=AllOptional):
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


class GuardhouseUpdate(GuardhouseBase):
    pass


class GuardhouseDelete(GuardhouseBase):
    pass


class GuardhouseResponse(Response):
    pass
