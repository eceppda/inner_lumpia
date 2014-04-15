from pyramid.view import view_config

@view_config(route_name='hello_json', renderer='json')
def hello_json(request):
    return [1, 2, 3]

@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    return {'project': 'inner_lumpia'}
