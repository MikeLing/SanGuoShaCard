import os
import logging
from random import shuffle, randint

from flask_cors import CORS
from flask_socketio import SocketIO, emit, join_room, leave_room
from flask import Flask, render_template, session, request, redirect, url_for

from src.data.data import GAMEDATA
from src.util.forms import LoginForm
from src.game_table.client import Client
from src.game_table.player import Player
from src.models.stage import Stage


LOG = logging.getLogger(__name__)
app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = 'secret!'

# avoid cors error
CORS(app)
socketio = SocketIO(app)


# all the player in this room
USERLIST = []

# game data for this room
hero_list = GAMEDATA.get_heroList()
card_list = GAMEDATA.get_cardHeap()

# game stage
STAGE = Stage.ending

# current player
playing_one = None


@app.route('/', methods=['GET', 'POST'])
def index():
    """Login form to enter a room."""
    form = LoginForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        session['room'] = form.room.data
        return redirect(url_for('game'))
    elif request.method == 'GET':
        form.name.data = session.get('name', '')
        form.room.data = session.get('room', '')
    return render_template('index.html', form=form)


@app.route('/game')
def game():
    """
        Chat room. The user's name and room must be stored in
        the session.
    """
    name = session.get('name', '')
    room = session.get('room', '')
    if name == '' or room == '':
        return redirect(url_for('index'))
    return render_template('game.html', name=name, room=room)


@socketio.on('start')
def start(message):
    """
        Start this game. Will assign two more cards to the player if that's his round.
    """
    global STAGE
    if STAGE == Stage.starting:
        emit('message', {'msg': 'warning!'}, room=request.sid)
    else:
        # choose one
        playing_one = USERLIST[randint(0, len(set(USERLIST)))]

        # recycle the card heap
        if len(card_list) < 2:
            card_list.append(GAMEDATA.get_cardHeap())
            shuffle(card_list)

        # give two more cards
        add_cards = card_list[0:2]
        c = playing_one.getPlayer().getCards()
        c += add_cards
        emit('assign', {
             'msg': {'cards': [i.title for i in c]}}, room=playing_one.getId())

        # start the game
        STAGE = Stage.starting


@socketio.on('joined')
def joined(message):
    """
        Sent by clients when they enter a room.
        A status message is broadcast to all people in the room.
    """

    room = session.get('room')
    # get the session id
    current_user = Client(request.sid)
    join_room(room)
    emit('status', {'msg': session.get('name') +
                    ' has entered the room.'}, room=room)

    # make sure there are enough slot for this user
    if len(hero_list) < 1 and len(card_list) < 4:
        emit('status',
             {'msg': session.get('name') + ' has entered the room. But no slot for him'}, room=current_user)
    else:
        # assign a hero and cards
        current_hero = hero_list.pop(-1)
        shuffle(card_list)
        current_cards = card_list[0:4]
        current_player = Player(request.sid)
        current_player.setCards(current_cards)
        current_player.setHero(current_hero)
        current_user.setPlayer(current_player)

        # append user into user list
        USERLIST.append(current_user)
        emit('player',
             {'msg': {'hero': [current_hero.name, current_hero.skill, current_hero.lifePoint],
                      'cards': [i.title for i in current_cards],
                      'name': session.get('name')}},
             room=request.sid)


@socketio.on('action')
def action(message):
    """
        Preformance the card action
    """
    


@socketio.on('text')
def text(message):
    """
        Sent by a client when the user entered a new message.
        The message is sent to all people in the room.
    """
    room = session.get('room')
    emit('message', {'msg': session.get('name') +
                     ':' + message['msg']}, room=room)


@socketio.on('left')
def left(message):
    """
        Sent by clients when they leave a room.
        A status message is broadcast to all people in the room.
    """
    room = session.get('room')
    leave_room(room)
    emit('status', {'msg': session.get('name') +
                    ' has left the room.'}, room=room)


if __name__ == '__main__':
    socketio.run(app, debug=True)
