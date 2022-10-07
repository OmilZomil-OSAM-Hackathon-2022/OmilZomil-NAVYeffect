from typing import List
from fastapi import APIRouter, Depends, Body
from sqlalchemy.orm import Session
from app.crud import user as crud
from app.schemas import user as schema
from app.api import deps


router = APIRouter()


@router.post("/", response_model=schema.UserResponse)
async def create_user(user: schema.UserCreate = Body(), db: Session = Depends(deps.get_db)):
    return crud.create_user(db, user)


@router.get("/", response_model=List[schema.UserRead])
def get_user(db: Session = Depends(deps.get_db)):
    return [schema.UserRead(user=user.user) for user in crud.get_user(db)]


@router.put("/information/{user_id}", response_model=schema.UserResponse)
async def update_user_information(user_id: int, information: schema.UserUpdateInformation = Body(), db: Session = Depends(deps.get_db)):
    return crud.update_user_information(db, user_id, information)


@router.put("/password/{user_id}", response_model=schema.UserResponse)
async def update_user_password(user_id: int, password: schema.UserUpdatePassword = Body(), db: Session = Depends(deps.get_db)):
    res = crud.update_user_password(db, user_id, password)
    if res is not None:
        res = schema.UserResponse(success=True, message="success")
    else:
        res = schema.UserResponse(success=False, message="entry not found")
    return res


@router.put("/role/{user_id}", response_model=schema.UserResponse)
async def update_user_role(user_id: int, role: schema.UserUpdateRole = Body(), db: Session = Depends(deps.get_db)):
    res = crud.update_user_role(db, user_id, role)
    if res is not None:
        res = schema.UserResponse(success=True, message="success")
    else:
        res = schema.UserResponse(success=False, message="entry not found")
    return res
