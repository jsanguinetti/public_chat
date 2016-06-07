from google.appengine.api import users
from flask import Blueprint, jsonify, request, json
from models.chat import chat_key_from_name
from models.message import Message

messages = Blueprint('messages', __name__)


@messages.route('/chats/<chat_name>/messages', methods=['POST'])
def message_post(chat_name):
    message = Message(parent=chat_key_from_name(chat_name),
                      content=request.form['content'],
                      user_id=users.get_current_user().user_id())
    message.put()
    # must handle json response in javascript.
    # important because we will use pusher
    return jsonify(message.to_dict())
