from flask import Blueprint, jsonify, request, json
from models.chat import chat_key_from_name
from models.message import Message
from google.appengine.api import memcache


messages = Blueprint('messages', __name__)


@messages.route('/chats/<chat_name>/messages', methods=['POST'])
def message_post(chat_name):
    message = Message(parent=chat_key_from_name(chat_name),
                      content=request.get_json()['content'])
    message.put()
    memcache.incr('message_count')
    # must handle json response in javascript.
    # important because we will use pusher
    return jsonify(message.to_dict())
