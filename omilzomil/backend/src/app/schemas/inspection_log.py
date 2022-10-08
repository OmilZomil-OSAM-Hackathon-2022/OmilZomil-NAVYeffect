from pydantic import BaseModel, Field
from app.db.base_schema import Response, AllOptional


class InspectionLogBase(BaseModel):
    access_id: int = Field(None, description="access id")
    affiliation: str = Field(None, description="affiliation")
    name: str = Field(None, description="name")
    rank: str = Field(None, description="rank")
    uniform: str = Field(None, description="uniform")
    has_name: bool = Field(None, description="has name")
    has_rank: bool = Field(None, description="has rank")
    has_neckerchief: bool = Field(None, description="has neckerchief and neckerchief ring")
    has_muffler: bool = Field(None, description="has muffler")
    has_flag: bool = Field(None, description="has flag")


class InspectionLogCreate(InspectionLogBase):
    pass


class InspectionLogRead(InspectionLogBase):
    inspection_id: int = Field(None, description="primary key")

    class Config:
        schema_extra = {
            "example": {
                "inspection_id": 1,
                "access_id": 1,
                "army_type": "해군",
                "name": "정의철",
                "rank": "병장",
                "uniform_type": "샘당",
                "has_name": True,
                "has_rank": True,
                "has_neckerchief": False,
                "has_muffler": False,
                "has_flag": False,
            }
        }
        orm_mode = True


class InspectionLogUpdate(InspectionLogBase, metaclass=AllOptional):
    class Config:
        schema_extra = {
            "example": {
                "uniform_type": "정복",
                "has_neckerchief": True,
                "has_muffler": True,
            }
        }


class InspectionLogResponse(Response):
    pass
