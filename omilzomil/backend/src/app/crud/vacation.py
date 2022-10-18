from datetime import date
import sqlalchemy.exc
from sqlalchemy.orm import Session
from app.models.vacation import Vacation
from app.schemas.vacation import VacationCreate, VacationRead, VacationUpdateConfirmation, VacationResponse


def create_vacation(db: Session, user_id: int, vacation: VacationCreate):
    if vacation.start_date > vacation.end_date:
        return VacationResponse(success=False, message="invalid start and end date")
    for entry in db.query(Vacation).filter_by(user=user_id).all():
        if vacation.end_date < entry.start_date:
            continue
        elif entry.end_date < vacation.start_date:
            continue
        return VacationResponse(success=False, message="overlapping vacation found")

    try:
        vacation = Vacation(user=user_id, start_date=vacation.start_date, end_date=vacation.end_date)
        db.add(vacation)
        db.commit()
        db.refresh(vacation)
        return VacationResponse(success=True, message=vacation.vacation_id)
    except sqlalchemy.exc.IntegrityError:
        return VacationResponse(success=False, message="foreign key constraint fail")


def get_vacations(db: Session, user_id: int):
    ret = list()
    for entry in db.query(Vacation).filter_by(user=user_id).order_by(Vacation.start_date).all():
        ret.append(
            VacationRead(
                vacation_id=entry.vacation_id,
                start_date=entry.start_date,
                end_date=entry.end_date,
                is_active=date.today() < entry.start_date,
                confirmed=entry.confirmed,
            )
        )
    return ret
