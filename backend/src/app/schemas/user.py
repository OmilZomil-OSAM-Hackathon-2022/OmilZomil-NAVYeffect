from pydantic import BaseModel, Field
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


class UserRead(UserBase, Response):
    user_id: int = Field(None, description="primary key")
    role: str = Field(None, description="role")

    class Config:
        schema_extra = {
            "example": {
                "success": True,
                "message": "success",
                "user_id": 1,
                "full_name": "정의철",
                "dog_number": "21-71007011",
                "affiliation": "해군",
                "military_unit": "계룡대 근무지원단 본부대대",
                "rank": "병장",
                "username": "21-71007011",
                "role": "super",
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
    role: str = Field(None, description="role")

    class Config:
        schema_extra = {
            "example": {
                "role": "admin",
            }
        }


class UserResponse(Response):
    user_id: int = Field(None, description="primary key")

    class Config:
        schema_extra = {
            "example": {
                "success": True,
                "message": "success",
                "user_id": 1,
            }
        }
