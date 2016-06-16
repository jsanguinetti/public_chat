from google.appengine.ext import ndb


class Chat(ndb.Model):
    name = ndb.StringProperty(required=True)
    description = ndb.StringProperty(required=True)

    def url_name(self):
        return self.name.replace(" ", "%20")


def chat_key_from_name(chat_name):
    return ndb.Key('Chat', chat_name)
