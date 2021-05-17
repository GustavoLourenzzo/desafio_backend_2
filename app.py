from flask import Flask, jsonify
from flask_cors import CORS
from db import registerMongoDB
from utils.http_response import invalid_route, method_allowed

from modules.swagger.Swagger import registerSwagger
from modules.users.users import users


app = Flask(__name__)


 # ******registra os modulos e extensoes ************
CORS(app) #liberação do das politicas do CORS
swagger = registerSwagger(app) #habilita o swagger e ativa o modulo aux
app.register_blueprint(users, url_prefix="/user") #modulo de usuario


#******** erros padroes ***********
app.register_error_handler(404, invalid_route)
app.register_error_handler(405, method_allowed)


# ****** banco de dados ***********
registerMongoDB(app)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)