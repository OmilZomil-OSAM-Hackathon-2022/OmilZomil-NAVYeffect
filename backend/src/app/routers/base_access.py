from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.db import get_db
import app.schemas.base_access as schema
import app.crud.base_access as crud


router = APIRouter(
    prefix="/access",
    tags=["부대 출입 정보"],
)


@router.get("/{access_id}", response_model=schema.BaseAccessRead)
async def get_access_log_by_id(access_id: int, db: Session = Depends(get_db)):
    access_log = crud.get_access_log_by_id(db, access_id)
    if access_log is None:
        access_log = schema.BaseAccessRead(success=False, message="Access log not found")
    return access_log
