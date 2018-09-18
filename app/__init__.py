from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options

from flask_login import LoginManager
from flask_mail import Mail
from flask_simplemde import SimpleMDE

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'github.login'

bootstrap = Bootstrap()
mail = Mail()
simple = SimpleMDE()


def create_app(config_name):
    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    # Initializing flask extensions
    bootstrap.init_app(app)
    mail.init_app(app)
    login_manager.init_app(app)
    simple.init_app(app)

    # Registering the  main blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # registering github blueprint
    from .github import github as github_blueprint
    app.register_blueprint(github_blueprint, url_prefix='/github_login')

    return app
