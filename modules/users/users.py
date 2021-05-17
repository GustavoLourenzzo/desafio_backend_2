from flask import Blueprint
from .routes import registerRoutes

users = Blueprint('users', __name__)

registerRoutes(users)
