from users import users
from auth import auth, requires_auth
from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

app.register_blueprint(users)
app.register_blueprint(auth)


@app.route('/')
@requires_auth
def hello_world():
    return jsonify({"message": "Hello World!"})


@app.errorhandler(404)
def not_found(error=None):
    resp = jsonify({'message': request.url + ' not found'})
    resp.status_code = 404
    return resp


@app.errorhandler(500)
def unknown_error(error=None):
    resp = jsonify({'message': error.message})
    resp.status_code = 500
    return resp


if __name__ == '__main__':
    app.run()
