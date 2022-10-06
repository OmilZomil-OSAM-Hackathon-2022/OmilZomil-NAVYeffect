from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.crud import base_access as crud
from app.schemas import base_access as schema
from app.api import deps


router = APIRouter()


@router.get("/{access_id}", response_model=schema.BaseAccessRead)
async def get_access_log_by_id(access_id: int, db: Session = Depends(deps.get_db)):
    access_log = crud.get_access_log_by_id(db, access_id)
    if access_log is None:
        access_log = schema.BaseAccessRead(success=False, message="Access log not found")
    return access_log
