from .controllers.UserController import UserController as uc

ROUTE = []

def registerRoutes(obj):
    for rt in ROUTE:

        obj.add_url_rule(rt['url'], methods=rt['methods'], view_func=rt['function'])


# ******************** Rotas do moedulo ***********************

ROUTE.append({'url': '/get/name', 'methods':['GET'],'function': uc.getUserByName})
ROUTE.append({'url': '/get/document', 'methods':['GET'],'function': uc.getUserByDocument})
ROUTE.append({'url': '/get/ilike', 'methods':['GET'],'function': uc.getUserByIlike})
ROUTE.append({'url': '/cadastra', 'methods':['POST'],'function': uc.cadastraUser})
ROUTE.append({'url': '/edita', 'methods':['PUT'],'function': uc.editaUser})
ROUTE.append({'url': '/deleta', 'methods':['DELETE'],'function': uc.deletaUser})


