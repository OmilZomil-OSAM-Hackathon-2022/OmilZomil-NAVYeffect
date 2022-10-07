from pydantic import BaseModel, Field
from app.db.base_schema import Response


class MilitaryUnitBase(BaseModel):
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


class MilitaryUnitResponse(Response):
    pass
