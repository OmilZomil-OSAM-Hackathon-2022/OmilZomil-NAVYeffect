from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from core.db import get_db
from app.enlisted_personnel.schema import EnlistedPersonnelRead, EnlistedPersonnelCreate
from app.enlisted_personnel import crud


router = APIRouter(
    prefix="/enlisted",
    tags=["장병 정보"],
)


@router.get("/create")
async def create_enlisted_personnel_entry(db: Session = Depends(get_db)):
    personnel = EnlistedPersonnelCreate(
        access_id=1,
        army_type="해군",
        name="정의철",
        rank="병장",
        uniform_type="샘당",
        has_name=True,
        has_rank=True,
        has_neckerchief=False,
        has_muffler=False,
        has_flag=False,
    )
    return crud.create_personnel(db=db, personnel=personnel)


@router.get("/read", response_model=List[EnlistedPersonnelRead])
async def read_all(db: Session = Depends(get_db)):
    persons = []
    i = 1
    while True:
        personnel = crud.get_personnel_by_id(db, i)
        if not personnel:
            break
        persons.append(personnel)
        i += 1
    return persons
