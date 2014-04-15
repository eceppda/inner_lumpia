from pyramid.httpexceptions import HTTPFound
from pyramid.response import Response
from pyramid.view import view_config


@view_config(route_name='hello_json', renderer='json')
def hello_json(request):
    return [1, 2, 3]


# First view, available at http://localhost:6543/
@view_config(route_name='home')
def home_view(request):
    return Response('<p>Visit <a href="/howdy?name=lisa">hello</a></p>')


@view_config(route_name='hello', renderer='hello_world.pt')
def hello_world(request):
    return dict(name=request.matchdict['name'])


# /goto which issues HTTP redirect to the last view
@view_config(route_name='redirect')
def redirect_view(request):
    return HTTPFound(location="/problem")


# /problem which causes an site error
@view_config(route_name='exception')
def exception_view(request):
    raise Exception()
