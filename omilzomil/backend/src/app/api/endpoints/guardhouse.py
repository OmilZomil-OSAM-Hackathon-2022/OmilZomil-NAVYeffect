from typing import List, Optional
from fastapi import APIRouter, Depends, Body
from sqlalchemy.orm import Session
from app.crud import guardhouse as crud
from app.schemas import guardhouse as schema
from app.api import deps


router = APIRouter()


@router.post("/", response_model=schema.GuardhouseResponse)
async def create_guardhouse(house: schema.GuardhouseCreate = Body(), db: Session = Depends(deps.get_db)):
    return crud.create_guardhouse(db, house.house)


@router.get("/", response_model=List[schema.GuardhouseRead])
def get_guardhouses(house: Optional[str] = None, db: Session = Depends(deps.get_db)):
    return crud.get_guardhouses(db, house)


@router.put("/{house_id}", response_model=schema.GuardhouseResponse)
async def update_guardhouse(house_id: int, new_house: schema.GuardhouseUpdate = Body(), db: Session = Depends(deps.get_db)):
    return crud.update_guardhouse(db, house_id, new_house.house)


@router.delete("/{house_id}", response_model=schema.GuardhouseResponse)
def delete_guardhouse(house_id: int, db: Session = Depends(deps.get_db)):
    return crud.delete_guardhouse(db, house_id)
