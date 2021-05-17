from flask_mongoengine import MongoEngine

config = {
    'db': 'desafio_back',
    'host': 'mongo',
    'port': 27017,
    'username': 'root',
    'password': 'senha123',
    'authentication_source': 'admin'
   
}

def registerMongoDB(app):
    app.config['MONGODB_SETTINGS'] = config
    db = MongoEngine()
    db.init_app(app)

