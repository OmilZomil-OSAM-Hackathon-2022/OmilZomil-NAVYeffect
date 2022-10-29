from typing import List, Optional
from fastapi import APIRouter, Depends, Body
from sqlalchemy.orm import Session
from app.crud import unit_house_relation as crud
from app.schemas import unit_house_relation as schema
from app.api import deps
from app.schemas.user import UserReadResponse


router = APIRouter()


@router.post("/{unit_id}", response_model=schema.UnitHouseRelationResponse)
async def create_unit_house_relation(
    unit_id: int,
    relation: schema.UnitHouseRelationCreate = Body(),
    db: Session = Depends(deps.get_db),
    current_user: UserReadResponse = Depends(deps.get_current_active_admin),
):
    if not current_user.success:
        return schema.UnitHouseRelationResponse(success=False, message=current_user.message)

    return crud.create_unit_house_relation(db, unit_id, relation.house_id)


@router.get("/{unit_id}", response_model=List[schema.UnitHouseRelationRead])
def get_unit_house_relations(
    unit_id: int, house: Optional[str] = None, db: Session = Depends(deps.get_db), current_user: UserReadResponse = Depends(deps.get_current_active_admin)
):
    if not current_user.success:
        return list()

    return crud.get_unit_house_relations(db, unit_id, house)


@router.delete("/{unit_id}/{house_id}", response_model=schema.UnitHouseRelationResponse)
def delete_unit_house_relation(
    unit_id: int, house_id: int, db: Session = Depends(deps.get_db), current_user: UserReadResponse = Depends(deps.get_current_active_admin)
):
    if not current_user.success:
        return schema.UnitHouseRelationResponse(success=False, message=current_user.message)

    return crud.delete_unit_house_relation(db, unit_id, house_id)
