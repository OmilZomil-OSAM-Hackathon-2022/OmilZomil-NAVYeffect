from app.models.guardhouse import Guardhouse


def get_guardhouse(db):
    model_list =  db.query(Guardhouse).all()
    return model_list


def select_guardhouse(db, house_name):
    print(house_name)
    return db.query(Guardhouse).filter(Guardhouse.house==house_name).order_by(Guardhouse.house).first().house_id


    pass