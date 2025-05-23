from flask import Flask
from flask_restx import Api
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from config import DevelopmentConfig

import os

bcrypt = Bcrypt()
jwt = JWTManager()
db = SQLAlchemy()


def create_app(config_class="config.DevelopmentConfig"):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Clés importantes
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'your_secret_key')

    # -----------------------------
    # JWT SETTINGS (access + refresh)
    # -----------------------------
    app.config['JWT_SECRET_KEY'] = app.config['SECRET_KEY']
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = 900  # 15 minutes
    app.config['JWT_REFRESH_TOKEN_EXPIRES'] = 2592000  # 30 days

    # Initialisation des extensions
    bcrypt.init_app(app)
    jwt.init_app(app)
    db.init_app(app)

    authorizations = {
        'Bearer': {
            'type': 'apiKey',
            'in': 'header',
            'name': 'Authorization'
        }
    }

    api = Api(app,
              version='1.0',
              title='HBnB API',
              description='HBnB Application API',
              authorizations=authorizations,
              security='Bearer'
              )
    CORS(app, supports_credentials=True)
    # Import et enregistrement des namespaces
    from app.api.v1.users import api as users_ns
    from app.api.v1.places import api as places_ns
    from app.api.v1.reviews import api as reviews_ns
    from app.api.v1.amenities import api as amenities_ns
    from app.api.v1.auth import api as auth_ns
    from app.api.v1.admin import api as admin_ns  # Import the admin namespace

    api.add_namespace(users_ns, path='/api/v1/users')
    api.add_namespace(places_ns, path='/api/v1/places')
    api.add_namespace(reviews_ns, path='/api/v1/reviews')
    api.add_namespace(amenities_ns, path='/api/v1/amenities')
    api.add_namespace(auth_ns, path='/api/v1/auth')
    # Register the admin namespace
    api.add_namespace(admin_ns, path='/api/v1/admin')

    return app
