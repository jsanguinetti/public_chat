from google.appengine.api import users, memcache


def url_links_processor(request):
    user = users.get_current_user()
    if user:
        url = users.create_logout_url(request.url)
        url_link_text = 'Logout'
    else:
        url = users.create_login_url(request.url)
        url_link_text = 'Login'
    return dict(url=url,
                url_link_text=url_link_text)