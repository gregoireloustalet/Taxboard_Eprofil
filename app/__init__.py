from flask import Flask, render_template, flash
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from app import config
from app.auth import auth
from app.database.database import DB
from app.models.user import User

#register all blueprints to app
def register_blueprints(app):
	app.register_blueprint(auth)


app = Flask(__name__)
Bootstrap(app)
login = LoginManager(app)
#app.config.from_object(config)
register_blueprints(app)

app.secret_key = 'top secret' # temporary


# Index route definition
@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
	return render_template('index.html')
	
@login.user_loader
def load_user(id):
	db = DB()
	if db.exists(id):
		user = User()
		user.fill(id)
		return user
	else:
		return None