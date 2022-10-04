from flask import Flask

# registering blueprints
from .views import views
from .auth import auth

# import sqlalchemy
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'cdcndjk cjwdkc wdkjcwebnfjkefjoijre fr'

    # config app for connecting it with database
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    # initialise the database by giving it the flask app
    db.init_app(app)

    # registering blueprints with app
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')


    return app