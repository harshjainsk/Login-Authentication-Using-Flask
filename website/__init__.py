from flask import Flask
from os import path


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

    """
    registering blueprints with app
    """
    # registering blueprints
    from .views import views
    from .auth import auth
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    # import models.py file
    from .models import User, Note

    # creating database app if not created
    create_database(app)

    return app


def create_database(app):
    """
        If the database is not created then it will create a
        database and store all the details in the database
        created, else it will wrote in the existing database
    """
    if not path.exists('website' + DB_NAME):
        db.create_all(app=app)
        print("Database Created!!!")
