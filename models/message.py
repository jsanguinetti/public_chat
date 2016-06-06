from google.appengine.ext import ndb


class Message(ndb.Model):
    content = ndb.StringProperty(indexed=False, required=True)
    date = ndb.DateTimeProperty(auto_now_add=True)
