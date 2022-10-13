from pydantic import BaseModel, Field
from typing import Optional
from app.db.base_schema import Response


class UserBase(BaseModel):
    full_name: str = Field(None, description="real user name")
    dog_number: str = Field(None, description="dog number")
    affiliation: str = Field(None, description="affiliation")
    military_unit: str = Field(None, description="military unit")
    rank: str = Field(None, description="rank")
    username: str = Field(None, description="username")


class UserCreate(UserBase):
    password: str = Field(None, description="password")

    class Config:
        schema_extra = {
            "example": {
                "full_name": "정의철",
                "dog_number": "21-71007011",
                "affiliation": "해군",
                "military_unit": "계룡대 근무지원단 본부대대",
                "rank": "병장",
                "username": "user",
                "password": "pass",
            }
        }


class UserFilter(UserBase):
    full_name: Optional[str] = Field(None, description="full name")
    affiliation: Optional[str] = Field(None, description="affiliation")
    military_unit: Optional[str] = Field(None, description="military unit")
    rank: Optional[str] = Field(None, description="rank")
    is_active: Optional[bool] = Field(None, description="is active")

    class Config:
        schema_extra = {
            "example": {
                "full_name": "정의철",
                "rank": "병장",
                "is_active": True,
            }
        }


class UserRead(UserBase):
    user_id: int = Field(None, description="primary key")
    role: int = Field(None, description="role")

    class Config:
        schema_extra = {
            "example": {
                "user_id": 1,
                "full_name": "정의철",
                "dog_number": "21-71007011",
                "affiliation": "해군",
                "military_unit": "계룡대 근무지원단 본부대대",
                "rank": "병장",
                "username": "21-71007011",
                "role": 1,
            }
        }
        orm_mode = True


class UserUpdateInformation(BaseModel):
    full_name: str = Field(None, description="real user name")
    dog_number: str = Field(None, description="dog number")
    affiliation: str = Field(None, description="affiliation")
    military_unit: str = Field(None, description="military unit")
    rank: str = Field(None, description="rank")

    class Config:
        schema_extra = {
            "example": {
                "full_name": "정의철",
                "dog_number": "21-71007011",
                "affiliation": "해군",
                "military_unit": "계룡대 근무지원단 본부대대",
                "rank": "병장",
            }
        }


class UserUpdatePassword(BaseModel):
    old_password: str = Field(None, description="old password")
    new_password: str = Field(None, description="new password")

    class Config:
        schema_extra = {
            "example": {
                "old_password": "old pass",
                "new_password": "new pass",
            }
        }


class UserUpdateRole(BaseModel):
    role: int = Field(None, description="role")

    class Config:
        schema_extra = {
            "example": {
                "role": 2,
            }
        }


class UserResponse(Response):
    pass
