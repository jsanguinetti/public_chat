from google.appengine.api import users, memcache
from flask import request, render_template, redirect, Blueprint
from models.chat import Chat, chat_key_from_name
from models.message import Message

chats = Blueprint('chats', __name__)


def memcache_message_count():
    if memcache.get('message_count') != None:
        message_count = memcache.get('message_count')
    else:
        message_count = 0
        memcache.set('message_count', 0)
    return message_count


@chats.route('/chats', methods=['GET'])
def chat_index():
    chat_query = Chat.query().order(-Chat.name)
    return render_template('chats.html',
                           chats=chat_query,
                           title='Chat List',
                           message_count=memcache_message_count())


@chats.route('/chats', methods=['POST'])
def chat_post():
    chat = Chat(id=request.form['name'],
                name=request.form['name'],
                description=request.form['description'])
    chat.put()
    chat.send_congratulations_email_to(users.get_current_user())
    return redirect('/chats')


@chats.route('/chats/<chat_name>')
def chat_show(chat_name):
    chat_key = chat_key_from_name(chat_name)
    chat = chat_key.get()
    reverse_query_messages = Message.query(ancestor=chat_key).order(-Message.date)
    messages = reversed(reverse_query_messages.fetch(10))
    return render_template('chat_view.html',
                           chat=chat,
                           current_user=users.get_current_user(),
                           messages=messages,
                           title=chat.name)

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
