from fastapi import APIRouter, Depends, Body
from sqlalchemy.orm import Session
from app.crud import inspection_log as crud
from app.schemas import inspection_log as schema
from app.api import deps


router = APIRouter()


@router.put("/{log_id}", response_model=schema.InspectionLogResponse)
async def update_inspection_log(log_id: int, log: schema.InspectionLogUpdate = Body(), db: Session = Depends(deps.get_db)):
    if crud.get_inspection_log_by_id(db, log_id) is not None:
        res = schema.InspectionLogResponse(success=True, message="success")
    else:
        res = schema.InspectionLogResponse(success=False, message="entry not found")
    return res
