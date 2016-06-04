# [START imports]
import urllib

from google.appengine.api import users
from google.appengine.ext import ndb

from flask import request, render_template, redirect, Blueprint

chats = Blueprint('chats', __name__)


# We set a parent key on the 'Greetings' to ensure that they are all
# in the same entity group. Queries across the single entity group
# will be consistent. However, the write rate should be limited to
# ~1/second.
class Chat(ndb.Model):
    name = ndb.StringProperty(required=True)
    description = ndb.StringProperty(required=True)


@chats.route('/chats', methods=['GET'])
def chat_index():
    chat_query = Chat.query().order(-Chat.name)
    return render_template('chats.html',
                           chats=chat_query,
                           title='Chat List')


@chats.route('/chats', methods=['POST'])
def chat_post():
    # Chat(name=request.args.get('name'),
    #      description=request.args.get('descriptions')).put()
    Chat(id=request.form['name'],
         name=request.form['name'],
         description=request.form['description']).put()
    return redirect('/chats')

# def chat_key(chat_name):
#     return ndb.Key('Chat', chat_name)
#
# # [START greeting]
# class Author(ndb.Model):
#     """Sub model for representing an author."""
#     identity = ndb.StringProperty(indexed=False)
#     email = ndb.StringProperty(indexed=False)
#
#
# class Greeting(ndb.Model):
#     """A main model for representing an individual Guestbook entry."""
#     author = ndb.StructuredProperty(Author)
#     content = ndb.StringProperty(indexed=False)
#     date = ndb.DateTimeProperty(auto_now_add=True)
#
#
# @chats.route('/')
# def hello_world():
#     chat_name = request.args.get('chat_name')
#     greetings_query = Greeting.query(
#         ancestor=chat_key(chat_name)).order(-Greeting.date)
#     greetings = greetings_query.fetch(10)
#     user = users.get_current_user()
#     return render_template('home.html',
#                            user=user,
#                            greetings=greetings,
#                            guestbook_name=urllib.quote_plus(chat_name))
#
#
# @chats.route('/sign', methods=['POST'])
# def sign():
#     chat_name = request.args.get('chat_name')
#     greeting = Greeting(parent=chat_key(chat_name))
#
#     if users.get_current_user():
#         greeting.author = Author(
#             identity=users.get_current_user().user_id(),
#             email=users.get_current_user().email())
#
#     greeting.content = request.form['content']
#     greeting.put()
#     query_params = {'chat_name': chat_name}
#     return redirect('/?' + urllib.urlencode(query_params))
