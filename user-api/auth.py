from functools import wraps
from flask import jsonify, request, Blueprint

auth = Blueprint('auth', __name__)


def check_auth():
    return request.headers.get('Authorization') is not None


def authenticate():
    resp = jsonify({'message': "Unauthorised, must sign in."})
    resp.status_code = 401
    return resp


def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not check_auth():
            return authenticate()

        return f(*args, **kwargs)

    return decorated
