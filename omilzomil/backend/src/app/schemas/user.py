from pydantic import BaseModel, Field
from typing import Optional
from app.db.base_schema import Response, AllOptional


class UserBase(BaseModel):
    full_name: str = Field(None, description="real user name")
    dog_number: str = Field(None, description="dog number")
    affiliation: int = Field(None, description="affiliation")
    military_unit: int = Field(None, description="military unit")
    rank: int = Field(None, description="rank")
    username: str = Field(None, description="username")


class UserCreate(UserBase):
    password: str = Field(None, description="password")

    class Config:
        schema_extra = {
            "example": {
                "full_name": "정의철",
                "dog_number": "21-71007011",
                "affiliation": 3,
                "military_unit": 2,
                "rank": 5,
                "username": "user",
                "password": "pass",
            }
        }


class UserFilter(UserBase):
    full_name: Optional[str] = Field(None, description="full name")
    affiliation: Optional[int] = Field(None, description="affiliation")
    military_unit: Optional[int] = Field(None, description="military unit")
    rank: Optional[int] = Field(None, description="rank")
    is_active: Optional[bool] = Field(None, description="is active")

    class Config:
        schema_extra = {
            "example": {
                "full_name": "정의철",
                "rank": 5,
                "is_active": True,
            }
        }


class UserRead(UserBase):
    user_id: int = Field(None, description="primary key")
    role: int = Field(None, description="role")
    is_active: bool = Field(None, description="is active")

    class Config:
        schema_extra = {
            "example": {
                "user_id": 1,
                "full_name": "정의철",
                "dog_number": "21-71007011",
                "affiliation": 3,
                "military_unit": 2,
                "rank": 5,
                "username": "21-71007011",
                "role": 3,
                "is_active": True,
            }
        }
        orm_mode = True


class UserReadResponse(UserRead, metaclass=AllOptional):
    success: Optional[bool] = Field(None, description="result")
    message: Optional[str] = Field(None, description="message")

    class Config:
        schema_extra = {
            "example": {
                "success": True,
                "message": "success",
                "user_id": 1,
                "full_name": "정의철",
                "dog_number": "21-71007011",
                "affiliation": 3,
                "military_unit": 2,
                "rank": 5,
                "username": "21-71007011",
                "role": 3,
            }
        }


class UserUpdateInformation(BaseModel):
    full_name: str = Field(None, description="real user name")
    dog_number: str = Field(None, description="dog number")
    affiliation: int = Field(None, description="affiliation")
    military_unit: int = Field(None, description="military unit")
    rank: int = Field(None, description="rank")

    class Config:
        schema_extra = {
            "example": {
                "full_name": "정의철",
                "dog_number": "21-71007011",
                "affiliation": 3,
                "military_unit": 2,
                "rank": 5,
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


class UserUpdateActivity(BaseModel):
    is_active: bool = Field(None, description="is active")

    class Config:
        schema_extra = {
            "example": {
                "is_active": True,
            }
        }


class UserResponse(Response):
    pass
