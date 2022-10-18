
from app.api.broker.broker import BrokerBase, SimpleBroker
from app.api.broker.image import ImageBroker


def create_broker(name, ws, id):
    brocker_list = {
        # "test" : BrokerBase,
        # "simple" : SimpleBroker,
        "image" : ImageBroker,
        "test" : ImageBroker,

    }
    return brocker_list[name](ws, id)