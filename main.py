import os
import logging
from random import shuffle, randint

from flask_cors import CORS
from flask_socketio import SocketIO, emit, join_room, leave_room
from flask import Flask, render_template, session, request, redirect, url_for

from src.data.data import GAMEDATA
from src.game_table.game import Game
from src.util.forms import LoginForm
from src.game_table.player import Player
from src.models.stage import Stage
from src.action.card_action import CardAction


LOG = logging.getLogger(__name__)
app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = 'secret!'

# avoid cors error
CORS(app)
socketio = SocketIO(app)

# game stage
STAGE = Stage.ending


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
        Game.room = session.get('room')
        Game.init_game_table()
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
    join_room(room)
    emit('status', {'msg': session.get('name') +
                    ' has entered the room.'}, room=room)

    # append user into user list
    Game.players.append(Player(request.sid))


# TODO:add js front and interact with it
@socketio.on('action')
def action(message):
    """
        Preformance the card action
    """
    # the target player
    target_id = message['target_player']
    using_card = message['card_id']

    # call card action and execute it.
    action = CardAction(request.sid)
    action.execute(request.sid, message.data)
    Game.actions.append(action)



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
