from pydantic import BaseModel, Field


# Shared Properties
class EnlistedPersonnelSchema(BaseModel):
    access_id: int = Field(title="출입기록 ID", description="int 형식의 출입기록 ID")
    army_type: str = Field(title="군 구분", description="str 형식의 소속 군 이름")
    name: str = Field(title="이름", description="str 형식의 병 이름")
    rank: str = Field(title="계급", description="str 형식의 병 계급")
    uniform_type: str = Field(title="복장 유형", description="str 형식의 복장 유형")
    has_name: bool = Field(title="이름표 부착 유무", description="bool 형식의 이름표 부착 유무")
    has_rank: bool = Field(title="계급장 부착 유무", description="bool 형식의 계급장 부착 유무")
    has_neckerchief: bool = Field(title="네커치프&네커치프 링 착용 유무", description="bool 형식의 네커치프&네커치프 링 착용 유무")
    has_muffler: bool = Field(title="머플러 착용 유무", description="bool 형식의 머플러 착용 유무")
    has_flag: bool = Field(title="태극기 부착 유무", description="bool 형식의 태극기 부착 유무")
