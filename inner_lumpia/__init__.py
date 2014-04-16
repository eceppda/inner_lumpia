from couchdb.client import Server
from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    config.registry.db_server = Server()

    def add_couchdb(request):
        db = config.registry.db_server[settings['couchdb.db']]
        return db

    config.add_request_method(add_couchdb, 'db', reify=True)
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('hello_json', '/json')
    config.scan()
    return config.make_wsgi_app()
