from pydantic import BaseModel, Field
from typing import Optional
from core.base_schema import AllOptional


class EnlistedPersonnelBase(BaseModel):
    success: Optional[bool] = Field(None, description="성공여부")
    message: Optional[str] = Field(None, description="실행결과")
    access_id: int = Field(None, description="출입기록 ID")
    army_type: str = Field(None, description="군 구분")
    name: str = Field(None, description="이름")
    rank: str = Field(None, description="계급")
    uniform_type: str = Field(None, description="복장 유형")
    has_name: bool = Field(None, description="이름표 부착 유무")
    has_rank: bool = Field(None, description="계급장 부착 유무")
    has_neckerchief: bool = Field(None, description="네커치프&네커치프 링 착용 유무")
    has_muffler: bool = Field(None, description="머플러 착용 유무")
    has_flag: bool = Field(None, description="태극기 부착 유무")


class EnlistedPersonnelCreate(EnlistedPersonnelBase):
    pass


class EnlistedPersonnelRead(EnlistedPersonnelBase, metaclass=AllOptional):
    class Config:
        schema_extra = {
            "example": {
                "success": True,
                "message": "Personnel info sucessfully read",
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


class EnlistedPersonnelUpdate(EnlistedPersonnelBase, metaclass=AllOptional):
    class Config:
        schema_extra = {
            "example": {
                "uniform_type": "정복",
                "has_neckerchief": True,
                "has_muffler": True,
            }
        }


class EnlistedPersonnelUpdateResult(EnlistedPersonnelUpdate):
    class Config:
        schema_extra = {
            "example": {
                "success": True,
                "message": "Personnel info sucessfully updated",
            }
        }
