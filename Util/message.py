"""
    A class to describle message bewteen clients(user)
"""

class Message(object):
    def __init__(self, action, data=None):
        self.action = action
        self.data = data
    
    def getAction(self):
        return self.action

    def setAction(self, action):
        self.action = action
    
    def getData(self):
        return self.data

    def setData(self, data):
        self.data = data