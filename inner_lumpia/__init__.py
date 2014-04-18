from couchdb.client import Server
from inner_lumpia.security import groupfinder
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    config.registry.db_server = Server()

    def add_couchdb(request):
        auth = open('/home/jeff/Source/inner_lumpia/.couch_auth', 'r')
        auth_pair = auth.readline()
        auth_pair = auth_pair.split(':')
        username = auth_pair[0]
        password = auth_pair[1]
        config.registry.db_server.resource.credentials = (username, password)
        db = config.registry.db_server[settings['couchdb.db']]
        return db

    config.add_request_method(add_couchdb, 'db', reify=True)

    authn_policy = AuthTktAuthenticationPolicy('seekrit',callback=groupfinder,  hashalg='sha512')
    authz_policy = ACLAuthorizationPolicy()
    config.set_authentication_policy(authn_policy)
    config.set_authorization_policy(authz_policy)

    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('hello', '/howdy')
    config.add_route('hello_json', '/json')
    config.add_route('login', '/login')
    config.add_route('logout', '/logout')
    config.scan()
    return config.make_wsgi_app()
