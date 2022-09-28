from typing import Optional
from pydantic import BaseModel, Field


from core.base_schema import AllOptional

# Shared properties
class UserBase(BaseModel):
    name: str = Field(title="성함", description='사용자 성함')
    uid: str
    password: str
    dog_num: str
    army: str
    unit: str
    rank: str


# Properties to receive on item creation
class UserCreate(UserBase):

    class Config:
        schema_extra = {
            "example": {
                "name": "홍길동",
                "uid": "11111",
                "password": "1234",
                "dog_num": "22-71001111",
                "army": "해군",
                "unit": "계룡대 근무지원단 본부대대",
                "rank": "일병",
            }
        }
    pass


# Properties to receive on item update
class UserUpdate(UserBase, metaclass=AllOptional):
    permission: int

    pass

class UserDisplay(UserBase):
    id: int
    permission: int

    class Config:
        orm_mode = True


# # Properties shared by models stored in DB
# class UserInDBBase(UserBase):
#     # id: int
#     # title: str
#     # owner_id: int

#     class Config:
#         orm_mode = True