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
                "name": "Foo",
                "uid": "A very nice Item",
                "password": "A very nice Item",
                "dog_num": "A very nice Item",
                "army": "A very nice Item",
                "unit": "A very nice Item",
                "rank": "A very nice Item",
            
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