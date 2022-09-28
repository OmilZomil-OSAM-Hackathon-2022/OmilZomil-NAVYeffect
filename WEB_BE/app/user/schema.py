from typing import Optional
from pydantic import BaseModel, Field


from core.base_schema import AllOptional

# Shared properties
class UserBase(BaseModel):
    name: str = Field(title="성함", description='사용자 성함')
    uid: str = Field(title="아이디", description='사용자 아이디 모두 유니크')
    password: str = Field(title="패스워드", description='비번은 알아서 잘 제한 없음')
    dog_num: str = Field(title="군번", description='군번은 태그가서있어서 문자열로 저장')
    army: str = Field(title="육해공군", description='육군 or 해군 or 공군 or 국직')
    unit: str = Field(title="소속", description='소속 부대 그냥 ipscan처럼 그대로 저장')
    rank: str = Field(title="계급", description='계급')


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