
from app.api.broker.broker import BrokerBase, SimpleBroker
from app.api.broker.image import ImageBroker, RandomImageBroker
from app.api.broker.worker import RandomSingleWorkerBroker

def create_broker(name, ws, id, db, guardhouse):
    brocker_list = {
        "test" : BrokerBase,
        "simple" : SimpleBroker,    # random ai - 이미지 저장 X
        "image" : ImageBroker,      # ai 없음 - 이미지 저장 O
        "random" : RandomImageBroker,
        "random_single" : RandomSingleWorkerBroker,
        "test" : RandomSingleWorkerBroker,

    }
    return brocker_list[name](ws, id, db, guardhouse)

