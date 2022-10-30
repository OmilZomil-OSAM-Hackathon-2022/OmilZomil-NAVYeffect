from string import ascii_letters
from random import randrange, choice
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from app.models.inspection_log import InspectionLog
from app.models.inspection_detail import InspectionDetail
from app.crud.military_unit import get_military_units
from app.crud.guardhouse import get_guardhouses


def create_test_case(db: Session):
    if not get_guardhouses(db):
        return {"success": False, "message": "guardhouse not found"}
    ids = [unit.unit_id for unit in get_military_units(db)]
    if not ids:
        return {"success": False, "message": "military unit not found"}

    for i in range(0, 10000):
        access_time = datetime.now() - timedelta(days=randrange(0, 365))

        base = InspectionLog(
            guardhouse=1,
            access_time=access_time,
            affiliation=randrange(1, 6),
            military_unit=ids[randrange(0, len(ids))],
            rank=randrange(1, 6),
            name="".join(choice(ascii_letters) for i in range(4)),
            uniform=randrange(1, 5),
            image_path=f"path{i}",
        )
        db.add(base)
        db.commit()
        db.refresh(base)

        appearance = randrange(0, 10) < 7
        for j in range(0, 7):
            if j == 0:
                status = randrange(0, 10) < 7
            else:
                if appearance:
                    status = True
                else:
                    status = bool(randrange(0, 2))

            log = InspectionDetail(
                inspection_id=base.inspection_id,
                appearance_type=j + 1,
                status=status,
                image_path=f"path{i}",
            )
            db.add(log)
            db.commit()
            db.refresh(log)
