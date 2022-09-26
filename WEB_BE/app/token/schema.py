from pydantic import BaseModel
from typing import Union



class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    """
    토큰에 들어갈 데이터
    """
    uid: Union[str, None] = None