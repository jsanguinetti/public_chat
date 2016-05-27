from functools import wraps
from flask import jsonify, request, Blueprint
from datetime import timedelta, datetime
import jwt

auth = Blueprint('auth', __name__)

SECRET_KEY = 'secret should be in environment variable, cannot do it now'


def check_auth():
    token = request.headers.get('Authorization')
    try:
        user_info = jwt.decode(token, SECRET_KEY)
    except jwt.ExpiredSignatureError:
        response = jsonify({'message':'Your JWT has expired'})
        response.status_code = 401
        return False
    except jwt.DecodeError:
        response = jsonify({'message': 'Your JWT has expired'})
        response.status_code = 401
        return False
    return True


def authenticate_message_response():
    resp = jsonify({'message': "Unauthorised, must sign in."})
    resp.status_code = 401
    return resp


def add_authentication_headers(resp, account):
    token = jwt.encode({'email': account.email,
                        'key': account.key.id(),
                        'exp': datetime.utcnow() + timedelta(minutes=60),
                        'iat': datetime.utcnow()}, SECRET_KEY)
    resp.headers['Authorization'] = token
    return resp


def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not check_auth():
            return authenticate_message_response()

        return f(*args, **kwargs)

    return decorated
