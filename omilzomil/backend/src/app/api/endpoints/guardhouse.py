from typing import Optional
from fastapi import APIRouter, Depends, Body
from fastapi_pagination import paginate, Page, Params
from sqlalchemy.orm import Session
from app.crud import guardhouse as crud
from app.schemas import guardhouse as schema
from app.api import deps
from app.schemas.user import UserReadResponse


router = APIRouter()


@router.post("/", response_model=schema.GuardhouseResponse)
async def create_guardhouse(
    house: schema.GuardhouseCreate = Body(), db: Session = Depends(deps.get_db), current_user: UserReadResponse = Depends(deps.get_current_active_super)
):
    if not current_user.success:
        return schema.GuardhouseResponse(success=False, message=current_user.message)

    return crud.create_guardhouse(db, house.house)


@router.get("/", response_model=Page[schema.GuardhouseRead])
async def get_guardhouses(house: Optional[str] = None, params: Params = Depends(), db: Session = Depends(deps.get_db)):
    return paginate(crud.get_guardhouses(db, house=house), params)


@router.put("/{house_id}", response_model=schema.GuardhouseResponse)
async def update_guardhouse(
    house_id: int,
    new_house: schema.GuardhouseUpdate = Body(),
    db: Session = Depends(deps.get_db),
    current_user: UserReadResponse = Depends(deps.get_current_active_super),
):
    if not current_user.success:
        return schema.GuardhouseResponse(success=False, message=current_user.message)

    return crud.update_guardhouse(db, house_id, new_house.house)


@router.delete("/{house_id}", response_model=schema.GuardhouseResponse)
def delete_guardhouse(house_id: int, db: Session = Depends(deps.get_db), current_user: UserReadResponse = Depends(deps.get_current_active_super)):
    if not current_user.success:
        return schema.GuardhouseResponse(success=False, message=current_user.message)

    return crud.delete_guardhouse(db, house_id)
