from pydantic import BaseModel, Field
from core.base_schema import AllOptional


class EnlistedPersonnelSchema(BaseModel):
    access_id: int = Field(title="출입기록 ID")
    army_type: str = Field(title="군 구분")
    name: str = Field(title="이름")
    rank: str = Field(title="계급")
    uniform_type: str = Field(title="복장 유형")
    has_name: bool = Field(title="이름표 부착 유무")
    has_rank: bool = Field(title="계급장 부착 유무")
    has_neckerchief: bool = Field(title="네커치프&네커치프 링 착용 유무")
    has_muffler: bool = Field(title="머플러 착용 유무")
    has_flag: bool = Field(title="태극기 부착 유무")


class EnlistedPersonnelCreate(EnlistedPersonnelSchema):
    class Config:
        schema_extra = {
            "example": {
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


class EnlistedPersonnelRead(EnlistedPersonnelSchema):
    class Config:
        orm_mode = True


class EnlistedPersonnelUpdate(EnlistedPersonnelSchema, metaclass=AllOptional):
    class Config:
        schema_extra = {
            "example": {
                "uniform_type": "정복",
                "has_neckerchief": True,
                "has_muffler": True,
            }
        }
