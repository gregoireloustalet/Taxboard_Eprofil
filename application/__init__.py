# Base config
from flask import Flask
from flask_bootstrap import Bootstrap
from application import config

# Required for Flask-login
from flask_login import LoginManager
from application.models.user import User

# Mail
from flask_mail import Mail

# Register all blueprints to app
from application.auth_blueprint import auth


def register_blueprints(app):
	app.register_blueprint(auth)


# Base config
app = Flask(__name__)
Bootstrap(app)
app.config.from_object(config.dev_config)
app.config.from_pyfile('application.cfg')
register_blueprints(app)

# Flask-Login
login = LoginManager(app)


@login.user_loader
def load_user(id):
	user = User()
	user.loaduser(id)
	return user

# Mail
mail = Mail(app)


"""
TO DO LATER -
protection vs csrf
from flask_wtf.csrf import CSRFProtect
csrf = CSRFProtect(app)
"""

import application.views
