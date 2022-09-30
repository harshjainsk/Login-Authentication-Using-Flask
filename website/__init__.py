from flask import Flask

# registering blueprints
from .views import views
from .auth import auth


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'cdcndjk cjwdkc wdkjcwebnfjkefjoijre fr'

    # registering blueprints with app
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')


    return app