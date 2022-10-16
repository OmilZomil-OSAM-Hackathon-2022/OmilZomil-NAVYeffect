from pydantic import BaseModel, Field


class AppearanceBase(BaseModel):
    appearance_id: int = Field(None, description="appearance id")
    appearance: str = Field(None, description="appearance")

    class Config:
        schema_extra = {
            "example": {
                "appearance_id": 1,
                "appearance": "두발",
            }
        }


class AppearanceRead(AppearanceBase):
    class Config:
        orm_mode = True
