# [START imports]
import urllib

from google.appengine.api import users
from google.appengine.ext import ndb
from models.message import Message

from flask import request, render_template, redirect, Blueprint

chats = Blueprint('chats', __name__)


@chats.route('/chats/<chat_name>/messages', methods=['POST'])
def message_post(chat_name):
    chat_key = ndb.Key('Chat', chat_name)
    # put_first_chat_message(chat_key)
    chat = chat_key.get()
    messages = Message.query(ancestor=chat_key).order(-Message.date)
    messages = messages.fetch(10)
    return render_template('chat_view.html',
                           chat=chat,
                           messages=messages,
                           title=chat.name)
