from datetime import datetime, timedelta
from pydantic import BaseModel, Field
from app.db.base_schema import Response, Omit


class VacationBase(BaseModel):
    user: int = Field(None, description="user id")
    start_date: datetime = Field(None, description="start date")
    end_date: datetime = Field(None, description="end date")


class VacationCreate(VacationBase):
    class Config:
        schema_extra = {
            "example": {
                "user": 1,
                "start_date": datetime.now(),
                "end_date": datetime.now() + timedelta(days=13),
            }
        }


class VacationRead(VacationBase, metaclass=Omit):
    vacation_id: int = Field(None, description="primary key")
    status: bool = Field(None, description="status")
    confirmed: bool = Field(None, description="confirmed")

    class Config:
        omit_fields = {"user"}
        schema_extra = {
            "example": {
                "vacation_id": 1,
                "start_date": datetime.now(),
                "end_date": datetime.now() + timedelta(days=13),
                "status": True,
                "confirmed": False,
            }
        }
        orm_mode = True


class VacationUpdateConfirmation(BaseModel):
    confirmed: bool = Field(None, description="confirmed")

    class Config:
        schema_extra = {
            "example": {
                "confirmed": True,
            }
        }


class VacationResponse(Response):
    pass
