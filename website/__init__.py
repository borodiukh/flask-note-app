from flask import Flask
from secrets import token_hex
from flask_login import LoginManager
from .models import session, User


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = token_hex(16)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return session.query(User).get(int(id))

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app

