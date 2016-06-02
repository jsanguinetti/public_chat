# [START imports]
from flask import Flask
from guestbooks import guestbooks

app = Flask(__name__)
app.config.from_object('config')
app.register_blueprint(guestbooks)


if __name__ == '__main__':
    app.run()
