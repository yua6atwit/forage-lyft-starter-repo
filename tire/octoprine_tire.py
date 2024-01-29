from tire.tire import tire

class octoprineTire(tire):
    def __init__(self, wear):
        self.wear = wear
    def needs_service(self):
        if sum(self.wear) >= 3.0:
            return True
        return False