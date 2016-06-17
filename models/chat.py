from google.appengine.ext import ndb
from google.appengine.api import mail


class Chat(ndb.Model):
    name = ndb.StringProperty(required=True)
    description = ndb.StringProperty(required=True)

    def url_name(self):
        return self.name.replace(" ", "%20")

    def send_congratulations_email_to(self, current_user):
        message = mail.EmailMessage(
            sender="no-reply@apps-escalables-public-chat.appspotmail.com",
            subject="Your chat '" + self.name + "' was created")
        message.to = (current_user.nickname() + " " + "<" + current_user.email() + ">")
        message.body = """Dear %s:
        Your chat '%s' has been created.  You can now visit
        https://apps-escalables-public-chat.appspot.com/chats/%s and sign in using your Google Account to
        access it.

        Please let us know if you have any questions.

        The PublicChat Team
        """ % (current_user.nickname(), self.name, self.url_name())
        message.send()
        pass


def chat_key_from_name(chat_name):
    return ndb.Key('Chat', chat_name)
