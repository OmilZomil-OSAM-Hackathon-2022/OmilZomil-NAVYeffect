from pydantic import BaseModel, Field


class RoleBase(BaseModel):
    role_id: int = Field(None, description="role id")
    role: str = Field(None, description="role")

    class Config:
        schema_extra = {
            "example": {
                "role_id": 1,
                "role": "user",
            }
        }


class RoleRead(RoleBase):
    class Config:
        orm_mode = True
