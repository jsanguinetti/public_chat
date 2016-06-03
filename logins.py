# [START imports]

from flask import render_template, Blueprint, url_for

logins = Blueprint('logins', __name__)


@logins.route('/login')
def login():
    return render_template('login.html', dog_url=url_for('static', filename='dog.png'))
