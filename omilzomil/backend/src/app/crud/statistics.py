from sqlalchemy.orm import Session, aliased
from app.models.inspection_log import InspectionLog
from app.models.inspection_detail import InspectionDetail
from app.schemas.Date import Date
from app.crud.military_unit import get_military_unit, get_military_units


def get_overall_stats(
    db: Session, date: Date, affiliation: int = None, military_unit: int = None, category: str = None, appearance_type: int = None, status: bool = None
):
    query = (
        db.query(InspectionLog)
        .join(InspectionDetail, InspectionLog.inspection_id == InspectionDetail.inspection_id)
        .filter(InspectionLog.access_time.like(str(date) + "%"))
    )

    if affiliation is not None:
        query = query.filter(InspectionLog.affiliation == affiliation)
    if military_unit is not None:
        query = query.filter(InspectionLog.military_unit == military_unit)
    if category == "hair":
        query = query.filter(InspectionDetail.appearance_type == 1)
    elif category == "appearance":
        query = query.filter(InspectionDetail.appearance_type > 1)
    if appearance_type is not None:
        query = query.filter(InspectionDetail.appearance_type == appearance_type)

    total = query.group_by(InspectionLog.inspection_id).count()
    if status is not None:
        count = query.filter(InspectionDetail.is_valid == True).filter(InspectionDetail.status == False).group_by(InspectionLog.inspection_id).count()
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
        subquery = (
            db.query(InspectionLog.inspection_id)
            .join(InspectionDetail, InspectionLog.inspection_id == InspectionDetail.inspection_id)
            .filter(InspectionLog.access_time.like(str(Date.now(day=False))))
            .filter(InspectionLog.military_unit == military_unit)
            .filter(InspectionDetail.status == False)
        )

        query = (
            db.query(InspectionLog.inspection_id, InspectionLog.name, InspectionLog.image_path)
            .filter(InspectionLog.access_time.like(str(Date.now(day=False))))
            .filter(InspectionLog.military_unit == military_unit)
            .filter(InspectionLog.inspection_id.not_in(subquery))
        )

        if query.count() == 0:
            return {"success": False, "message": "no entry found"}
        else:
            res = query.first()
            return {"name": res.name, "image_path": res.image_path}

    return ret
