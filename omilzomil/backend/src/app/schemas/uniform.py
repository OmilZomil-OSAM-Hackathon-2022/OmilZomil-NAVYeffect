from pydantic import BaseModel, Field


class UniformBase(BaseModel):
    uniform_id: int = Field(None, description="uniform id")
    uniform: str = Field(None, description="uniform")

    class Config:
        schema_extra = {
            "example": {
                "uniform_id": 1,
                "uniform": "샘당",
            }
        }


class UniformRead(UniformBase):
    class Config:
        orm_mode = True
