from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import crud, schemas
from app.api import deps


router = APIRouter()


@router.get("/{access_id}", response_model=schemas.base_access.BaseAccessRead)
async def get_access_log_by_id(access_id: int, db: Session = Depends(deps.get_db)):
    access_log = crud.base_access.get_access_log_by_id(db, access_id)
    if access_log is None:
        access_log = schemas.base_access.BaseAccessRead(success=False, message="Access log not found")
    return access_log
