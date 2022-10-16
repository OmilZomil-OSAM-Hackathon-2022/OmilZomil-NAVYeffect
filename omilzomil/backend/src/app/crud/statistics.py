from datetime import datetime
from sqlalchemy import or_
from sqlalchemy.orm import Session, aliased
from app.models.access_log import AccessLog
from app.models.inspection_log import InspectionLog
from app.models.inspection_detail import InspectionDetail
from app.crud.military_unit import get_military_unit, get_military_units


def get_monthly_overall_stats(db: Session, military_unit: int = None, date: datetime = None, category: str = None, status: bool = None):
    if date is None:
        date = datetime.now()

    query = (
        db.query(InspectionLog)
        .join(AccessLog, AccessLog.access_id == InspectionLog.access_id)
        .join(InspectionDetail, InspectionLog.inspection_id == InspectionDetail.inspection_id)
        .filter(AccessLog.access_time.like(date.strftime("%Y-%m-%%")))
    )

    if military_unit is not None:
        query = query.filter(or_(AccessLog.military_unit == military_unit))
    if category == "hair":
        query = query.filter(InspectionDetail.appearance_type == 1)
    elif category == "appearance":
        query = query.filter(InspectionDetail.appearance_type > 1)

    total = query.group_by(InspectionLog.inspection_id).count()
    if status is not None:
        count = query.filter(InspectionDetail.status == False).group_by(InspectionLog.inspection_id).count()
        if status:
            count = total - count
    else:
        count = total

    return (total, count)


def get_monthly_detailed_stats(db: Session, appearance_type: int, military_unit: int = None, date: datetime = None, status: bool = None):
    if date is None:
        date = datetime.now()

    query = (
        db.query(InspectionLog)
        .join(AccessLog, AccessLog.access_id == InspectionLog.access_id)
        .join(InspectionDetail, InspectionLog.inspection_id == InspectionDetail.inspection_id)
        .filter(AccessLog.access_time.like(date.strftime("%Y-%m-%%")))
        .filter(InspectionDetail.appearance_type == appearance_type)
    )

    if military_unit is not None:
        query = query.filter(or_(AccessLog.military_unit == military_unit))
    if status is not None:
        count = query.filter(InspectionDetail.status == status).count()
    else:
        count = query.count()

    return count


def take_fourth(elem):
    return elem[3]


def get_monthly_unit_ranks(db: Session):
    entries = list()
    for unit in get_military_units(db):
        total, count = get_monthly_overall_stats(db, military_unit=unit.unit_id, status=True)
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
