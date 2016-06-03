# [START imports]

from filters.context_processors import url_links_processor
from filters.login_filter import login_filter
from flask import Flask, request
from guestbooks import guestbooks
from logins import logins

app = Flask(__name__)
app.register_blueprint(logins)
app.register_blueprint(guestbooks)


@app.context_processor
def inject_base_template_vars():
    return url_links_processor(request)


@app.before_request
def before_request():
    return login_filter(request)


if __name__ == '__main__':
    app.run()
