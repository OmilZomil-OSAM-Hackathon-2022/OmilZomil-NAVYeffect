from pydantic import BaseModel, Field


class AffiliationBase(BaseModel):
    affiliation_id: int = Field(None, description="affiliation id")
    affiliation: str = Field(None, description="affiliation")

    class Config:
        schema_extra = {
            "example": {
                "affiliation_id": 1,
                "affiliation": "육군",
            }
        }


class AffiliationRead(AffiliationBase):
    class Config:
        orm_mode = True
