# SanGuoShaCard
A test from PingCap which is about to deliver a backend of SanGuoSha game.

## Blueprint for this Project
This project will contains follow components:

### A server:

- waitting and listening the 'join' request from User

- a message queue to schdule users into 'Game table' 

- Create a instantiation of the 'Game table'(players, roles, the Cards etc)

- tear down the 'Ganme table' after the end of the game

(greate to have but may not happened this time)

- authentication (due to I have no plane to use any database in this project)

- let user can choose a role by himself (same reason above)

- Allow mutiple instantiation of 'Game table' on the server in the same time(Maybe docker can help us create instantiation for 'Game table', but man, just leave it alone :/ )

- Maybe rsomething like Redis can help us schdule user into game table faster, but :)

### Game table:

- User List: The users on this Game table.

- User: card of this user, Life point, A timer(each user only have 30 seconds for each round), role(Master, good guy, Bad guy)

- Heap: Cards can assign, shuffle the heap randomly.

- Recycle Heap: Recording the cards already been used (I think it's same data structer with 'Heap' and we can swap them directly after 'Heap' been run out)

- Juge: Search all the status of player after one player quit from the game table and juge who win this game(Bad guy will win after the master dead or all other people dead, the Master and good guy win when all the bad guy win)

(greate to have but may not happened this time)

- Hero (That's too complex to happened, at least for now)