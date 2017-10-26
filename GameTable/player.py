class player(object):
    
    def __init__(self, id, senderClient):
        self.id = id
        self.sender = senderClient

        self.lifePoint = 0
        self.maxLifePoint = 0

        # Hero
        self.hero = None

        # weapon card
        self.warpon = None
        self.armor = None
        self.plus = None
        self.minus = None
        self.cards = []

        # game rule
        self.supplyShortage = None
        self.indulgence = None
    
    def getSender(self):
        return self.sender

    def getId(self):
        return self.id

    def getMaxLifePoint(self):
        return self.maxLifePoint

    def setMaxLifePoint(self):
        