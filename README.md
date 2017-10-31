# SanGuoShaCard
A test from PingCap which is about to deliver a backend of SanGuoSha game.

## Blueprint for this Project

### Framework

Websocket(Flask_SocketIO) + Flask

### Work Flow

The work flow for this project can be separated into **3** stage: join stage, playing stage, ending

#### Join stage:

A player client will send a join request to server which includes the player id, requested room size, game type and some other game conditions, then waiting. The server will first put that request into the 'waiting room' and search condition fitting room on the room list. The server will return the room id and all the player list as return if it found a game room can be join. Otherwise, the server will create a empty room for that player and return a room id after that.

![picture](https://github.com/MikeLing/SanGuoShaCard/blob/master/doc/server_client.jpg)

#### Playing stage:
After all players be 'seperated' into a same room, all the game logic and game flow contoring will been done in the room instance, and the server will only works as a message dispatcher and receiver. After player send a 'Action'(game action or card action) to the client, the client will package that action with player id and room id and send to the server. The server will accept it and dispatch the message to correspond room. Then, inside the room,it will unpackages the message and begin a series of game logic dealing.  The data will be sended as brodcast message to everyone in that room so all the players can update the other players' status and game stage, after the game logic done.

![picture](https://github.com/MikeLing/SanGuoShaCard/blob/master/doc/cs2.jpg)

And the server's message dealing flow are shown as follow:
![picture](https://github.com/MikeLing/SanGuoShaCard/blob/master/doc/client_flow.jpg)

#### Ending stage:
After the game end, the server will broadcast the ending message to all the clients. After all the session on that room ended, the server will recycle all the memory assigned to that room.


#### class design
Some core classes are shown as follow:

![picture](https://github.com/MikeLing/SanGuoShaCard/blob/master/doc/Untitled.jpg)
### Milestone

~~define basic data models~~

~~define core models for game~~

~~define cards, hero and other useful data structures~~

~~login and send message to other player~~

~~Assign cards and hero to player~~

~~define card action like slah（杀）, dodge（闪）, peach（桃）~~

~~add api for card action~~

add js and fornt to interact with back end

add unit test for all the models

Add database to instead of hard code Singleton data model 
