from datetime import datetime
from sqlalchemy.orm import Session, aliased
from app.models.access_log import AccessLog
from app.models.inspection_log import InspectionLog
from app.models.inspection_detail import InspectionDetail
from app.schemas.Date import Date
from app.crud.military_unit import get_military_unit, get_military_units


def create_test_case(db: Session):
    from string import ascii_letters
    from random import randrange, choice
    from datetime import timedelta

    ids = [unit.unit_id for unit in get_military_units(db)]
    if not ids:
        return {"success": False, "message": "military unit not found"}

    for i in range(0, 10000):
        access_time = datetime.now() - timedelta(days=randrange(0, 365))

        base = AccessLog(military_unit=ids[randrange(0, len(ids))], access_time=access_time)
        db.add(base)
        db.commit()
        db.refresh(base)

        base = InspectionLog(
            access_id=base.access_id,
            affiliation=randrange(1, 6),
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


def get_overall_stats(
    db: Session, date: Date, affiliation: int = None, military_unit: int = None, category: str = None, appearance_type: int = None, status: bool = None
):
    query = (
        db.query(InspectionLog)
        .join(AccessLog, AccessLog.access_id == InspectionLog.access_id)
        .join(InspectionDetail, InspectionLog.inspection_id == InspectionDetail.inspection_id)
        .filter(AccessLog.access_time.like(str(date) + "%"))
    )

    if affiliation is not None:
        query = query.filter(InspectionLog.affiliation == affiliation)
    if military_unit is not None:
        query = query.filter(AccessLog.military_unit == military_unit)
    if category == "hair":
        query = query.filter(InspectionDetail.appearance_type == 1)
    elif category == "appearance":
        query = query.filter(InspectionDetail.appearance_type > 1)
    if appearance_type is not None:
        query = query.filter(InspectionDetail.appearance_type == appearance_type)

    total = query.group_by(InspectionLog.inspection_id).count()
    if status is not None:
        count = query.filter(InspectionDetail.status == False).group_by(InspectionLog.inspection_id).count()
        if status:
            count = total - count
    else:
        count = total

    return (total, count)


def take_fourth(elem):
    return elem[3]


def get_monthly_unit_ranks(db: Session):
    entries = list()
    for unit in get_military_units(db):
        total, count = get_overall_stats(db, date=Date.now(day=False), military_unit=unit.unit_id, status=True)
        if total == 0:
            rate = 0
        else:
            rate = round(count / total * 100)
        entries.append([unit.unit, count, total - count, rate])
    entries.sort(key=take_fourth, reverse=True)

    ret = list()
    for i in range(0, len(entries)):
        entry = {
            "rank": i + 1,
            "unit": entries[i][0],
            "pass": entries[i][1],
            "fail": entries[i][2],
            "pass_rate": entries[i][3],
        }
        ret.append(entry)

    return ret


def get_monthly_best_stats(db: Session, military_unit: int, category: str):
    ret = dict()

    if category == "unit":
        res = get_monthly_unit_ranks(db)
        unit = get_military_unit(db, military_unit)
        for i in range(0, len(res)):
            if res[i]["unit"] == unit.unit:
                ret = {"unit": unit.unit, "rank": res[i]["rank"]}
                break
    elif category == "person":
        query = (
            db.query(AccessLog.access_id)
            .filter(AccessLog.access_time.like(datetime.now().strftime("%Y-%m-%%")))
            .filter(AccessLog.military_unit == military_unit)
        )

        subquery = (
            db.query(AccessLog.access_id)
            .join(InspectionLog, AccessLog.access_id == InspectionLog.access_id)
            .join(InspectionDetail, InspectionLog.inspection_id == InspectionDetail.inspection_id)
            .filter(AccessLog.access_time.like(datetime.now().strftime("%Y-%m-%%")))
            .filter(AccessLog.military_unit == military_unit)
            .filter(InspectionDetail.status == False)
        )

        subquery = query.filter(InspectionLog.inspection_id.not_in(subquery))
        InspectionLogAlias = aliased(InspectionLog)

        res = (
            db.query(AccessLog.access_id, InspectionLogAlias.name, InspectionLogAlias.image_path)
            .select_from(InspectionLogAlias)
            .join(AccessLog, AccessLog.access_id == InspectionLogAlias.access_id)
            .filter(AccessLog.access_id.in_(subquery))
            .first()
        )

        return {"name": res.name, "image_path": res.image_path}

    return ret
