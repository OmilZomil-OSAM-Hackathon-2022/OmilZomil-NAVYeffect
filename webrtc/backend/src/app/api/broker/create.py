
from app.api.broker.broker import BrokerBase, SimpleBroker


def create_broker(name, ws, id):
    brocker_list = {
        "test" : BrokerBase,
        # "test" : SimpleBroker,

    }
    return brocker_list[name](ws, id)