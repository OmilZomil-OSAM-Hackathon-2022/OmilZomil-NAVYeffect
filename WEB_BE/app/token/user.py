from fastapi import Depends, HTTPException, status

from sqlalchemy.orm import Session

from jose import JWTError, jwt

from core.db import get_db
from app.token.jwt import verify_password, oauth2_scheme, SECRET_KEY, ALGORITHM
from app.token.schema import TokenData
from app.user.crud import get_user_by_uid

async def get_current_user(db:Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    """
    토큰을 가져와 현재 유저를 가져온다
    """
    
    # 예외 선언
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        # 토큰 해독
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        # 인증받은 값 추출
        uid: str = payload.get("uid")
        if uid is None:
            raise credentials_exception

        token_data = TokenData(uid=uid)
    except JWTError:
        raise credentials_exception

    # DB 에서 사용자 조회
    user = get_user_by_uid(db, uid=token_data.uid)
    if user is None:
        raise credentials_exception
    return user



def authenticate_user(db: Session, uid: str, pw: str):
    """
    유저조회
    """
    user = get_user_by_uid(db, uid)
    if not user:
        return False
    if not verify_password(pw, user.password):
        return False
    return user