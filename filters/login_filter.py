from google.appengine.api import users
from flask import redirect


def login_filter(request):
    if '/login' not in request.url:
        if not users.get_current_user():
            return redirect(users.create_login_url(request.url))
