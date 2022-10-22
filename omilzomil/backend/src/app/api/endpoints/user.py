from typing import Optional
from fastapi import APIRouter, Depends, Body
from fastapi_pagination import paginate, Page, Params
from sqlalchemy.orm import Session
from app.crud import user as crud
from app.schemas import user as schema
from app.api import deps
from app.schemas.user import UserReadResponse


router = APIRouter()


@router.post("/", response_model=schema.UserResponse)
async def create_user(user: schema.UserCreate = Body(), db: Session = Depends(deps.get_db)):
    return crud.create_user(db, user)


@router.get("/", response_model=Page[schema.UserRead])
async def get_users(
    full_name: Optional[str] = None,
    affiliation: Optional[int] = None,
    military_unit: Optional[int] = None,
    rank: Optional[int] = None,
    is_active: Optional[bool] = None,
    params: Params = Depends(),
    db: Session = Depends(deps.get_db),
    current_user: UserReadResponse = Depends(deps.get_current_active_admin),
):
    if not current_user.success:
        return list()

    flt = schema.UserFilter(full_name=full_name, affiliation=affiliation, military_unit=military_unit, rank=rank, is_active=is_active)
    return paginate(crud.get_users(db, flt), params)


@router.put("/information/{user_id}", response_model=schema.UserResponse)
async def update_user_information(
    user_id: int,
    information: schema.UserUpdateInformation = Body(),
    db: Session = Depends(deps.get_db),
    current_user: UserReadResponse = Depends(deps.get_current_active_user),
):
    if not current_user.success:
        return schema.UserResponse(success=False, message=current_user.message)

    return crud.update_user_information(db, user_id, information)


@router.put("/password/{user_id}", response_model=schema.UserResponse)
async def update_user_password(
    user_id: int,
    password: schema.UserUpdatePassword = Body(),
    db: Session = Depends(deps.get_db),
    current_user: UserReadResponse = Depends(deps.get_current_active_user),
):
    if not current_user.success:
        return schema.UserResponse(success=False, message=current_user.message)

    return crud.update_user_password(db, user_id, password)


@router.put("/role/{user_id}", response_model=schema.UserResponse)
async def update_user_role(
    user_id: int,
    role: schema.UserUpdateRole = Body(),
    db: Session = Depends(deps.get_db),
    current_user: UserReadResponse = Depends(deps.get_current_active_super),
):
    if not current_user.success:
        return schema.UserResponse(success=False, message=current_user.message)

    return crud.update_user_role(db, user_id, role)


@router.put("/activity/{user_id}", response_model=schema.UserResponse)
async def update_user_activity(
    user_id: int,
    is_active: schema.UserUpdateActivity = Body(),
    db: Session = Depends(deps.get_db),
    current_user: UserReadResponse = Depends(deps.get_current_active_admin),
):
    if not current_user.success:
        return schema.UserResponse(success=False, message=current_user.message)

    return crud.update_user_activity(db, user_id, is_active)


@router.delete("/{user_id}", response_model=schema.UserResponse)
def delete_user(
    user_id: int,
    password: schema.UserDelete = Body(),
    db: Session = Depends(deps.get_db),
    current_user: UserReadResponse = Depends(deps.get_current_active_user),
):
    if not current_user.success:
        return schema.UserResponse(success=False, message=current_user.message)

    return crud.delete_user(db, user_id, password)
