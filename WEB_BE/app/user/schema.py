from typing import Optional
from pydantic import BaseModel, Field


from core.schema_core import AllOptional

# Shared properties
class UserBase(BaseModel):
    name: str = Field(title="aaaaa", description='qqqqq')
    uid: str
    password: str
    dog_num: str
    army: str
    unit: str
    rank: str


# Properties to receive on item creation
class UserCreate(UserBase):
    pass


# Properties to receive on item update
class UserUpdate(UserBase, metaclass=AllOptional):
    disable: bool

    pass

class UserDisplay(UserBase):
    id: int
    disable: bool

    class Config:
        orm_mode = True


# # Properties shared by models stored in DB
# class UserInDBBase(UserBase):
#     # id: int
#     # title: str
#     # owner_id: int

#     class Config:
#         orm_mode = True