from users import users
from flask import Flask
from flask import jsonify

app = Flask(__name__)

app.register_blueprint(users)


@app.route('/')
def hello_world():
    return jsonify({"message": "Hello World!"})


if __name__ == '__main__':
    app.run()
