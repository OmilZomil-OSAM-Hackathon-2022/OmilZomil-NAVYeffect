from typing import List, Optional
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
def get_users(
    full_name: Optional[str] = None,
    affiliation: Optional[int] = None,
    military_unit: Optional[int] = None,
    rank: Optional[int] = None,
    is_active: Optional[bool] = None,
    db: Session = Depends(deps.get_db),
):
    flt = schema.UserFilter(full_name=full_name, affiliation=affiliation, military_unit=military_unit, rank=rank, is_active=is_active)
    return crud.get_users(db, flt)


@router.put("/information/{user_id}", response_model=schema.UserResponse)
async def update_user_information(user_id: int, information: schema.UserUpdateInformation = Body(), db: Session = Depends(deps.get_db)):
    return crud.update_user_information(db, user_id, information)


@router.put("/password/{user_id}", response_model=schema.UserResponse)
async def update_user_password(user_id: int, password: schema.UserUpdatePassword = Body(), db: Session = Depends(deps.get_db)):
    return crud.update_user_password(db, user_id, password)


@router.put("/role/{user_id}", response_model=schema.UserResponse)
async def update_user_role(user_id: int, role: schema.UserUpdateRole = Body(), db: Session = Depends(deps.get_db)):
    return crud.update_user_role(db, user_id, role)


@router.put("/activity/{user_id}", response_model=schema.UserResponse)
async def update_user_activity(user_id: int, is_active: schema.UserUpdateActivity = Body(), db: Session = Depends(deps.get_db)):
    return crud.update_user_activity(db, user_id, is_active)


@router.delete("/{user_id}", response_model=schema.UserResponse)
def delete_user(user_id: int, password: schema.UserDelete = Body(), db: Session = Depends(deps.get_db)):
    return crud.delete_user(db, user_id, password)
