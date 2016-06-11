from flask import Blueprint, jsonify, request, json, render_template
from models.chat import chat_key_from_name
from models.message import Message
from google.appengine.api import memcache
from google.appengine.api import search

_INDEX_NAME = 'messages'

messages = Blueprint('messages', __name__)


def create_document(message_dict):
    return search.Document(
        fields=[search.TextField(name='user', value=message_dict['user']['nickname']),
                search.TextField(name='content', value=message_dict['content'])])


@messages.route('/chats/<chat_name>/messages', methods=['POST'])
def message_post(chat_name):
    message = Message(parent=chat_key_from_name(chat_name),
                      content=request.get_json()['content'])
    message.put()
    memcache.incr('message_count')
    message_dict = message.to_dict()
    search.Index(name=_INDEX_NAME).put(create_document(message_dict))
    return jsonify(message_dict)


@messages.route('/messages', methods=['GET'])
def message_search():
    query = request.args.get('search')
    query_obj = search.Query(query_string=query)
    results = search.Index(name=_INDEX_NAME).search(query=query_obj)
    return render_template('message_result_page.html',
                           results=results)
