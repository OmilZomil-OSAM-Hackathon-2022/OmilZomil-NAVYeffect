
from app.api.broker.broker import BrokerBase, SimpleBroker
from app.api.broker.image import ImageBroker
from app.api.broker.worker import RandomSingleBroker

def create_broker(name, ws, id):
    brocker_list = {
        "test" : BrokerBase,
        "simple" : SimpleBroker,
        "image" : ImageBroker,
        "random" : RandomWorkBroker,
        # "test" : RandomWorkBroker,

    }
    return brocker_list[name](ws, id)

def create_await_broker(name, ws, id):
    brocker_list = {
        "test" : SimpleBroker,
        #"test" : RandomSingleBroker,

    }
    return brocker_list[name](ws, id)