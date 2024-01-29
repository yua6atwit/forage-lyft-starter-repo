from tire.tire import tire

class carriganTire(tire):
    def __init__(self, wear):
        self.wear = wear
    def needs_service(self):
        for w in self.wear:
            if w >= 0.9:
                return True
        return false
        