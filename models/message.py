from google.appengine.ext import ndb
from google.appengine.api import users


class Message(ndb.Model):
    content = ndb.StringProperty(indexed=False, required=True)
    date = ndb.DateTimeProperty(auto_now_add=True)
    user = ndb.UserProperty(auto_current_user=True)

    def to_dict(self):
        result = super(Message, self).to_dict()
        result['user'] = self.get_user_dict()
        return result

    def get_user_dict(self):
        dictionary = {}
        user = self.user
        dictionary['email'] = user.email()
        dictionary['user_id'] = user.user_id()
        dictionary['nickname'] = user.nickname()
        return dictionary
