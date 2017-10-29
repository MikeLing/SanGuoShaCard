"""
    A class to describle message bewteen clients(user)
"""


class Message(object):
    def __init__(self, action=None, data=None):
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

    def addData(self, key, value):
        if self.data == None:
            self.data = {}
        self.data[key] = value


if __name__ == '__main__':
    import json
    mockMessage = Message()
    mockMessage.setAction("Test")
    mockMessage.addData("id", 1)
    mockMessage.addData("data", 12345)
    string = json.dumps(mockMessage.__dict__)
    print string
