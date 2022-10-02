from pydantic import BaseModel, Field
from typing import Union



class Token(BaseModel):
    access_token: str = Field(title="접속 토큰", description='실제 토큰')
    token_type: str = Field(title="토큰 타입", description='추후 변경시 사용 용도')


class TokenData(BaseModel):
    """
    토큰에 들어갈 데이터
    """
    uid: Union[str, None] = Field(title=" 유저 아이디", description='사용자 식별 용도')
