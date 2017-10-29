import json
from src.util.message import Message
from src.util.singleton import Singleton


class Server(object):
    connections = []

    @staticmethod
    def getConnections():
        """
        Get the connection list
        
        Return:
            connections
        """
        return Server.connections

    @staticmethod
    def addConnections(connection):
        """
        Add connection into the connection list
        
        Args:
            connection(Client): The connection been added
                into connection list
        """
        Server.connections.append(connection)
    
    @staticmethod
    def broadcast(message):
        """
        Broadcast message to other clients
        
        Args:
            message(Message): The message will been broadcase
        """
        for client in Server.connections:
            try:
                payload = json.dumps(message.__dict__, ensure_ascii = False).encode('utf8')
                client.sendMessage(payload, isBinary = False)
            except IOError as e:
                print "Get an error in gameServer!"
