from pydantic import BaseModel, Field
from app.db.base_schema import Response


class InspectionDetailUpdateStatus(BaseModel):
    status: bool = Field(None, description="status")

    class Config:
        schema_extra = {
            "example": {
                "status": True,
            }
        }


class InspectionDetailUpdateValidity(BaseModel):
    is_valid: bool = Field(None, description="is valid")

    class Config:
        schema_extra = {
            "example": {
                "is_valid": True,
            }
        }


class InspectionDetailResponse(Response):
    pass
