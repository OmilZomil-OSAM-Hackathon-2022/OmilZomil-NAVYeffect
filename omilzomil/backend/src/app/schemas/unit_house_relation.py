from pydantic import BaseModel, Field
from app.db.base_schema import Response
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
