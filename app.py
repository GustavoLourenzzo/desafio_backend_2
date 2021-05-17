from flask import Flask, jsonify
from flask_cors import CORS
from db import registerMongoDB

from modules.swagger.Swagger import registerSwagger
from modules.users.users import users


app = Flask(__name__)


 # ******registra os modulos e extensoes ************
CORS(app) #liberação do das politicas do CORS
swagger = registerSwagger(app) #habilita o swagger e ativa o modulo aux
app.register_blueprint(users, url_prefix="/user") #modulo de usuario


# ****** banco de dados ***********
registerMongoDB(app)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)