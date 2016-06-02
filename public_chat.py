# [START imports]
from google.appengine.api import users

from flask import Flask, request
from guestbooks import guestbooks

app = Flask(__name__)
app.config.from_object('config')
app.register_blueprint(guestbooks)


@app.context_processor
def inject_base_template_vars():
    user = users.get_current_user()
    if user:
        url = users.create_logout_url(request.url)
        url_link_text = 'Logout'
    else:
        url = users.create_login_url(request.url)
        url_link_text = 'Login'
    return dict(url=url,
                url_link_text=url_link_text)


if __name__ == '__main__':
    app.run()
