from flask import (
	current_app, request, redirect, url_for, render_template, flash, abort,
)

from flask_login import login_user, login_required, logout_user
from ..auth import auth

from application.forms.registerForm import RegisterForm
from application.forms.loginForm import LoginForm
from application.database import get_db
from application.models.session import Session
from application.models.user import User


# Login
@auth.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	# on POST
	if form.validate_on_submit():
		# Try to fetch user to check if he exists, and verify password
		db = get_db()
		doc_id = form.session.genID()
		doc = db.fetch(doc_id)
		if doc != None:
			session = Session()
			session.fromJSON(doc.value)
			if (session.validates(form.password.data)):
				# Create class for flask-login, and create the session
				user = User()
				user.fill(doc_id)
				login_user(user)
				flash('you were successfully logged in as ' + session.email)
				return redirect(url_for('index'))
			
			#else, show error
			else:
				flash('Login error', 'error')
		else:
			flash('Login error', 'error')
	return render_template('login.html', form=form)
	
# Logout
@auth.route('/logout', methods=['GET'])
@login_required
def logout():
	logout_user()
	flash('You were logged out', 'success')
	return redirect(url_for('index'))
	

# Register
@auth.route('/register', methods=['GET', 'POST'])
def register():
	form = RegisterForm()
	if form.validate_on_submit():
		db = get_db()
		if db.exists(form.session.genID()):
			flash('User already exists', 'error')
		else:
			db.insert(form.session.genID(), form.session.toJSON())
			flash('User created', 'success')
			return redirect(url_for('index'))
	
	return render_template('register.html', form=form)