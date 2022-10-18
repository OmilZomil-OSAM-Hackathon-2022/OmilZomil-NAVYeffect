import sqlalchemy.exc
from sqlalchemy.orm import Session
from app.models.user import User
from app.models.vacation import Vacation
from app.schemas.vacation import VacationCreate, VacationUpdateApproval, VacationResponse


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


def get_vacations(db: Session, user_id: int = None, unit_id: int = None):
    query = db.query(Vacation)
    if user_id is not None:
        query = query.filter_by(user=user_id)
    elif unit_id is not None:
        query = query.join(User, Vacation.user == User.user_id).filter(User.military_unit == unit_id).filter(Vacation.is_approved == None)
    return query.order_by(Vacation.start_date.desc()).all()


def update_vacation_approval(db: Session, vacation_id: int, is_approved: VacationUpdateApproval):
    vacation = db.query(Vacation).filter_by(vacation_id=vacation_id)
    if not vacation.count():
        return VacationResponse(success=False, message="entry not found")
    elif type(is_approved.is_approved) != bool:
        return VacationResponse(success=False, message="invalid type")
    else:
        vacation.update(is_approved.dict())
        db.commit()
        return VacationResponse(success=True, message=vacation_id)


def delete_vacation(db: Session, vacation_id: int):
    vacation = db.query(Vacation).filter_by(vacation_id=vacation_id)
    if not vacation.count():
        return VacationResponse(success=False, message="entry not found")
    elif vacation.is_approved is True:
        return VacationResponse(success=False, message="already approved")
    else:
        vacation.delete()
        db.commit()
        return VacationResponse(success=True, message=vacation_id)
