from flask import jsonify
from flask import Blueprint

users = Blueprint('users', __name__)


@users.route('/users/')
def index():
    return jsonify({"message": "users index placeholder"});
