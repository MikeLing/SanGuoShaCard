import json
from Util.message import Message

class Singleton:
    """
    A non-thread-safe helper class to ease implementing singletons.
    This should be used as a decorator -- not a metaclass -- to the
    class that should be a singleton.

    The decorated class can define one `__init__` function that
    takes only the `self` argument. Also, the decorated class cannot be
    inherited from. Other than that, there are no restrictions that apply
    to the decorated class.

    To get the singleton instance, use the `Instance` method. Trying
    to use `__call__` will result in a `TypeError` being raised.

    """

    def __init__(self, decorated):
        self._decorated = decorated

    def Instance(self):
        """
        Returns the singleton instance. Upon its first call, it creates a
        new instance of the decorated class and calls its `__init__` method.
        On all subsequent calls, the already created instance is returned.

        """
        try:
            return self._instance
        except AttributeError:
            self._instance = self._decorated()
            return self._instance

    def __call__(self):
        raise TypeError('Singletons must be accessed through `Instance()`.')

    def __instancecheck__(self, inst):
        return isinstance(inst, self._decorated)

@Singleton
class Server:
    def __init__(self):
        self.connections = []

    def getConnections(self):
        """
        Get the connection list
        
        Return:
            connections
        """
        return self.connections

    def addConnections(self, connection):
        """
        Add connection into the connection list
        
        Args:
            connection(Client): The connection been added
                into connection list
        """
        self.connections.append(connection)
    
    def broadcast(self, message):
        """
        Broadcast message to other clients
        
        Args:
            message(Message): The message will been broadcase
        """
        for client in self.connections:
            try:
                payload = json.dumps(message, ensure_ascii = False).encode('utf8')
                client.sendMessage(payload, isBinary = False)
            except IOError as e:
                print "Get an error in gameServer!"


GAMESERVER = Server.Instance()
