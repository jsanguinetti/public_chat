from filters.context_processors import url_links_processor
from filters.login_filter import login_filter
from flask import Flask, request, redirect
from chats import chats
from logins import logins
from messages import messages

app = Flask(__name__)
app.register_blueprint(logins)
app.register_blueprint(chats)
app.register_blueprint(messages)


@app.route('/')
def home():
    return redirect('/chats')


@app.context_processor
def inject_base_template_vars():
    return url_links_processor(request)


# @app.before_request
# def before_request():
#     return login_filter(request)


if __name__ == '__main__':
    app.run()
