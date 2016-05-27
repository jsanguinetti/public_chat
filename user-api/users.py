from flask import jsonify, request, Blueprint, json
from google.appengine.ext import ndb
from model_utils import ModelUtils

users = Blueprint('users', __name__)
from werkzeug.security import generate_password_hash, \
    check_password_hash


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
    user = Account(email=request.get_json()['email'],
                   pw_hash=generate_password_hash(request.get_json()['password']))
    user.put()
    return jsonify({"message": user.to_dict()});
