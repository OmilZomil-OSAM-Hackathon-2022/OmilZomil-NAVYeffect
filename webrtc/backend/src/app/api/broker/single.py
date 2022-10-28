from app.api.broker.base import BaseBroker



class SingleBroker(BaseBroker):
    
    
    def __init__(self, id, db):
        super().__init__(id)
        self.db = db
        
        pass