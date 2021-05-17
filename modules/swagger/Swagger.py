
from flasgger import Swagger
from flask import Blueprint

template = {
  "swagger": "2.0",
  "info": {
    "title": "Desafio Backend 2",
    "description": "Descrição dos endpoints validos da api",
    "contact": {
    #   "responsibleOrganization": "ME",
      "responsibleDeveloper": "Gustavo lourenzzo",
      "email": "me@me.com",
    #   "url": "www.me.com",
    },
    "termsOfService": "/swagger/termos",
    "version": "1.0.0"
  },
  "host": "localhost",  # overrides localhost:500
  "basePath": "/",  # base bash for blueprint registration
  "schemes": [
    "http",
    "https"
  ],
  "operationId": "getmyData"
}

swagger_config = {
    "headers": [
    ],
    "specs": [
        {
            "endpoint": 'apispec_1',
            "route": '/apispec_1.json',
            "rule_filter": lambda rule: True,  
            "model_filter": lambda tag: True,
        }
    ],
    
    "static_url_path": "/flasgger_static",
    # "static_folder": "static",  # must be set by user
    "swagger_ui": True,
    "specs_route": "/swagger/apidocs/"
}
swagger_bp = Blueprint('swagger_bp', __name__)

@swagger_bp.route('/termos', methods=['GET'])
def index():
    return "Termos de uso -- livre para todos os usos."

def registerSwagger(app):
    app.register_blueprint(swagger_bp, url_prefix="/swagger") #modulo auxliar swagger
    swagger = Swagger(app, config=swagger_config, template=template)
    return swagger