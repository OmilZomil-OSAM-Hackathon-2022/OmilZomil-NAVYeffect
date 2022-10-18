from datetime import date, timedelta
from pydantic import BaseModel, Field
from app.db.base_schema import Response


class VacationBase(BaseModel):
    start_date: date = Field(None, description="start date")
    end_date: date = Field(None, description="end date")


class VacationCreate(VacationBase):
    class Config:
        schema_extra = {
            "example": {
                "start_date": date.today(),
                "end_date": date.today() + timedelta(days=13),
            }
        }


class VacationRead(BaseModel):
    vacation_id: int = Field(None, description="primary key")
    start_date: date = Field(None, description="start date")
    end_date: date = Field(None, description="end date")
    is_approved: bool = Field(None, description="is_approved")

    class Config:
        omit_fields = {"user"}
        schema_extra = {
            "example": {
                "vacation_id": 1,
                "start_date": date.today(),
                "end_date": date.today() + timedelta(days=13),
                "is_approved": None,
            }
        }
        orm_mode = True


class VacationUpdateApproval(BaseModel):
    is_approved: bool = Field(None, description="is_approved")

    class Config:
        schema_extra = {
            "example": {
                "is_approved": True,
            }
        }


class VacationResponse(Response):
    pass
