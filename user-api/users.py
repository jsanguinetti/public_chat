from flask import jsonify, request, Blueprint, json
from google.appengine.ext import ndb
from model_utils import ModelUtils
from auth import add_authentication_headers
from werkzeug.security import generate_password_hash, check_password_hash

users = Blueprint('users', __name__)


class Account(ModelUtils, ndb.Model):
    email = ndb.StringProperty(required=True)
    pw_hash = ndb.StringProperty(required=True)
    created = ndb.DateTimeProperty(auto_now_add=True)
    verification_hash = ndb.StringProperty()
    verified = ndb.DateTimeProperty()

    def to_dict(self):
        result = super(Account, self).to_dict()
        result.pop('pw_hash')
        result.pop('verification_hash')
        result.pop('verified')
        return result


@users.route('/users', methods=['GET'])
def index():
    return jsonify({"message": "user index placeholder"});


@users.route('/users', methods=['POST'])
def create():
    accounts = Account.query(Account.email == request.get_json()['email'])
    if accounts.get():
        resp = jsonify({"message": "user already exists"})
        resp.status_code = 422
        return resp
    else:
        user = Account(email=request.get_json()['email'],
                       pw_hash=generate_password_hash(request.get_json()['password']))
        user.put()
        return jsonify({"message": user.to_dict()})


@users.route('/users/authenticate', methods=['POST'])
def authenticate():
    account = Account.query(Account.email == request.get_json()['email']).get()
    authenticated = (account is not None) & check_password_hash(account.pw_hash, request.get_json()['password'])
    if authenticated:
        return add_authentication_headers(jsonify(account.to_dict()), account)
    else:
        resp = jsonify({"message": 'Wrong email or password'})
        resp.status_code = 401
        return resp
