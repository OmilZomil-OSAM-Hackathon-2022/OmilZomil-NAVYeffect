from datetime import datetime
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from core.db import get_db
from app.base_access.schema import BaseAccessRead, BaseAccessCreate
from app.base_access import crud


router = APIRouter(
    prefix="/access",
    tags=["부대 출입 정보"],
)


@router.get("/create")
async def create_enlisted_personnel_entry(db: Session = Depends(get_db)):
    personnel = BaseAccessCreate(
        base_name="계룡대 1정문",
        access_time=datetime.now(),
        image=b"123",
    )
    return crud.create_access(db=db, access=personnel)


@router.get("/read", response_model=List[BaseAccessRead])
async def read_all(db: Session = Depends(get_db)):
    logs = []
    i = 1
    while True:
        access = crud.get_access_by_id(db, i)
        if not access:
            break
        logs.append(access)
        i += 1
    return logs
