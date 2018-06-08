from flask import Flask, render_template
from app import config
from app.auth import auth

#register all blueprints to app
def register_blueprints(app):
	app.register_blueprint(auth)


app = Flask(__name__)
#app.config.from_object(config)
register_blueprints(app)

app.secret_key = 'top secret' # temporary


# Index route definition
@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
	return render_template('index.html')