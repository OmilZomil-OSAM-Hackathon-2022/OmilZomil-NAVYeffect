from pydantic import BaseModel, Field


class RankBase(BaseModel):
    rank_id: int = Field(None, description="rank id")
    rank: str = Field(None, description="rank")

    class Config:
        schema_extra = {
            "example": {
                "rank_id": 1,
                "rank": "이병",
            }
        }


class RankRead(RankBase):
    class Config:
        orm_mode = True
