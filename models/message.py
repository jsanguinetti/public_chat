from google.appengine.ext import ndb
from google.appengine.api import users


class Message(ndb.Model):
    content = ndb.StringProperty(indexed=False, required=True)
    date = ndb.DateTimeProperty(auto_now_add=True)
    user_id = ndb.StringProperty()

    def to_dict(self):
        result = super(Message, self).to_dict()
        result.__delitem__('user_id')
        result['user'] = self.get_user_dict()
        return result

    def get_user(self):
        return users.User(_user_id=self.user_id)

    def get_user_dict(self):
        dictionary = {}
        user = self.get_user()
        dictionary['email'] = user.email()
        dictionary['user_id'] = user.user_id()
        dictionary['nickname'] = user.nickname()
        return dictionary
