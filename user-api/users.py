from flask import jsonify, Blueprint
from google.appengine.ext import ndb
from flask import current_app as app
# from flask_bcrypt import Bcrypt
#
# bcrypt = Bcrypt(app)

users = Blueprint('users', __name__)


class Account(ndb.Model):
    email = ndb.StringProperty(required=True)
    pw_hash = ndb.StringProperty(required=True)
    created = ndb.DateTimeProperty(auto_now_add=True)
    verification_hash = ndb.StringProperty()
    verified = ndb.DateTimeProperty()


@users.route('/users/')
def index():
    return jsonify({"message": "users index placeholder"});
